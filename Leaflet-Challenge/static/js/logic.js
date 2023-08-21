// Set URL for API pull
let url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";


// Function to create map
function createMap(earthquakes){
      // Create the tile layer that will be the background of our map.
    let mapBase = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    // Create map object
    let map = L.map("map", {
        center: [39.50, -98.35],
        zoom: 5,
        layers: [mapBase, earthquakes]


    });

    // Create a legend to display information about our map.
    let legend = L.control({
        position: "bottomright"
    });
    
    // When the layer control is added, insert a div with the class of "legend".
    legend.onAdd = function() {
        let div = L.DomUtil.create("div", "legend")
        grades = [-10, 10, 30, 50, 70, 90];

    // loop through the grades and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
        return div;
    };
    // Add the info legend to the map.
    legend.addTo(map);
};


// Create function to color markers based on earthquake depth
function getColor(d) {
    return d > 90 ? '#FF0D0D' :
           d > 70  ? '#FF4E11' :
           d > 50  ? '#FF8E15' :
           d > 30  ? '#FAB733' :
           d > 10   ? '#ACB334' :
                      '#69B34C';
};


// Create function to plot markers
function createMarkers(response){
    // Defining the features property from the response data
    let earthquake = response.features;

    // Initialize an array to hold earthquake markers
    let earthquakeMarkers = [];

    // Loop through the response data
    for (let i=0; i<earthquake.length; i++){
        // Defining each row in the response data
        let row = earthquake[i];

        // Defining variables to hold select output
        let lat = row.geometry.coordinates[1]
        let lon = row.geometry.coordinates[0]
        let depth = row.geometry.coordinates[2]
        let title = row.properties.title
        let magnitude = row.properties.mag
        
        // For each earthquake, create the marker, customize the markers
        // Also bind a popup with the title of the earthquake
        let earthquakeMarker = L.circle([lat, lon], {
            fillOpacity: 0.5,
            weight: 1,
            color: "white",
            fillColor: getColor(depth),
            radius: (magnitude) * 20000
        })
        .bindPopup(title + "</br> Depth: " + depth)

        // Push the markers to the earthquake markers array
        earthquakeMarkers.push(earthquakeMarker)
    };

    // Create a layer group from the earthquake marker array
    // Call back the create map function
    createMap(L.layerGroup(earthquakeMarkers))    
};

// Perform API call then call createMarkers function
d3.json(url).then(createMarkers);