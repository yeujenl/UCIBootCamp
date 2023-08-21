# Import the dependencies.
import numpy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
mt = Base.classes.measurement
st = Base.classes.station

query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365) 

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Main route listing all API routes
@app.route("/")
def welcome():
    """List all aviailable API Routes."""
    return(
        f"<h3>Available Routes:</h3>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/yyyy-mm-dd(search_start_date)<br>"
        f"/api/v1.0/yyyy-mm-dd(search_start_date))/yyyy-mm-dd(search_end_date)<br>"
        )

# Route for precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    # Query returning date and precipitation date from measurement table
    # Filtered for date occuring on and after query date  
    prcp_results = session.query(mt.date, mt.prcp).\
        filter(mt.date >= query_date).all()
    
    # Close session
    session.close

    # Open empty precipitation list to record output
    precipitation = []

    # For loop through the query results
    for date, prcp in prcp_results:
        # Open empty dicitionary
        prcp_dict = {}

        # Write output into dictionary
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp

        # Append dictionary to precipitation list
        precipitation.append(prcp_dict)
    
    # Jsonify the output
    return jsonify(precipitation)
    

# Route for stations
@app.route("/api/v1.0/stations")
def station_api():
    session = Session(engine)

    # Query returning staion number and station name date from station table
    station_results = session.query(st.station, st.name).all()

    # Close session
    session.close

    # Open empty station_info list to record output
    station_info = []

    # For loop through the query results
    for station_no, station_name in station_results:
        # Open empty dicitionary
        station_dict = {}

        # Write output into dictionary
        station_dict["station_no"] = station_no
        station_dict["station_name"] = station_name

        # Append dictionary to station list
        station_info.append(station_dict)
    
    # Jsonify the output
    return jsonify(station_info)


# Route for tobs
@app.route("/api/v1.0/tobs")
def tobs_api():
    session = Session(engine)

    # Query returning date and tobs date from measurement table
    # Filtered for date occuring on and after query date and highest traffic station  
    tobs_results = session.query(mt.date, mt.tobs).\
        filter(mt.date >= query_date).\
        filter(mt.station == "USC00519281").all()
    
    # Close session
    session.close

    # Open empty tobs_info list to record output
    tobs_info = []

    # For loop through the query results
    for date, tobs in tobs_results:
        # Open empty dicitionary
        tobs_dict = {}

        # Write output into dictionary
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs

        # Append dictionary to station list
        tobs_info.append(tobs_dict)
    
    # Jsonify the output
    return jsonify(tobs_info)
    

# Route for start date
@app.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)

    # String format the input date
    date_str = str(start)

    # Template to format date_str
    format_str = "%Y-%m-%d"
    
    # Standardize start date input
    start_date = dt.datetime.strptime(date_str, format_str).date()

    # Query returning date and tobs date from measurement table
    # Functions to calculate the minimum, average and maximum temperature
    # Filtered for date ocurring on and after the start date
    # Group by the dates
    start_date_results = session.query(mt.date, func.min(mt.tobs), func.avg(mt.tobs), func.max(mt.tobs)).\
        filter(mt.date >= start_date).\
        group_by(mt.date).all()
    
    # Close session
    session.close

    # List comprehension to create list of dictionary to record outputs 
    start_date_output = [{"date": s_output[0], 
                          "min_temp": s_output[1], 
                          "avg_temp": s_output[2], 
                          "max_temp": s_output[3]} for s_output in start_date_results]

    # Jsonify the output
    return jsonify(start_date_output)
    

# Route for start date and end date
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = Session(engine)
    # Template to format date_str
    format_str = "%Y-%m-%d"

    # String format the input dates
    s_date_str = str(start)
    e_date_str = str(end)
    
    # Standardize start date and end date input
    start_date = dt.datetime.strptime(s_date_str, format_str).date()
    end_date = dt.datetime.strptime(e_date_str, format_str).date()

    # Query returning date and tobs date from measurement table
    # Functions to calculate the minimum, average and maximum temperature
    # Filtered for date ocurring on and after the start date and on and before the end date
    # Group by the dates
    se_date_results = session.query(mt.date, func.min(mt.tobs), func.avg(mt.tobs), func.max(mt.tobs)).\
        filter(mt.date >= start_date, mt.date <= end_date).\
        group_by(mt.date).all()
    
    # Close session
    session.close
    
    # List comprehension to create list of dictionary to record outputs 
    se_date_output = [{"date": se_output[0], 
                          "min_temp": se_output[1], 
                          "avg_temp": se_output[2], 
                          "max_temp": se_output[3]} for se_output in se_date_results]

    # Jsonify the output
    return jsonify(se_date_output)


if __name__ == '__main__':
    app.run(debug=True)
