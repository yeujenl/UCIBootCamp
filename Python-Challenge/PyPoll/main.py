# Importing modules
import os
import csv

# Creating input path for csv file
election_csv = os.path.join("Resources","election_data.csv")

# Defining tracking variables to start at 0
total_votes = 0
candidate_votes = 0

# Opening list to save candidate data from csv file
candidate_vote_data = []

# Opening list to save printed results in list
print_result = []

# Opening dictionary to store candidate vote calculations
candidates_dictionary = {}

# Opening csv file to read as csv file
with open(election_csv, "r", encoding="utf-8") as csvfile:
    # Reading csv file with "," as delimiter
    csvreader = csv.reader(csvfile, delimiter=",")
    # Pulling out header row
    csv_header = next(csvreader)

    # For loop to pull the information from the csv reader
    for row in csvreader:
        # Count the total number of votes 
        total_votes = total_votes + 1
        # Pulling out the candidate column (index 2) to write to candidate_vote_date list
        candidate_vote_data.append(row[2])

# Sort candidate_vote_data by alphabetical order
sorted_candidate_data = sorted(candidate_vote_data)

# Create a candidate list consisting of only unique candidate names
# Sorted by alphabetical order
candidate_list = sorted(list(set(sorted_candidate_data)))

# Nested for loop running the candidate vote data against the candidate name list
for candidate_name in candidate_list:
    for row in sorted_candidate_data:

        # Conditional if candidate name matches increase candidate vote count by 1   
        if row == candidate_name:
            candidate_votes = candidate_votes + 1
        
        # Conditional if candidate name match does not match candidate vote
        # Wrap up current candidate vote count to move to next candidate
        else:
            # Increase candidate vote count by 1 to account for last count
            candidate_votes = candidate_votes + 1
            # Creating variable to write to candidate dictionary
            # Key: candidate's name, value: total vote count for candidate
            candidate_data = {candidate_name:candidate_votes}
            # Update the candidate dictionary with the candidate_data variable
            candidates_dictionary.update(candidate_data)
            # Change the candidate_name variable to the current row (new candidate name)
            candidate_name = row
            # Resetting candidate vote counter to 0
            candidate_votes = 0

# Defining function to calculate the candidate vote percentage
def percentage_calculation (candidate_vote_count):
    # Setting the candidate_total_vote variable
    # Wrapped as interger for calculation
    candidate_total_vote=int(candidate_vote_count)
    
    # Calculate the candidate's vote as a percentage of the total vote count
    # Round to 3 decimal places
    candidate_percentage = round((candidate_total_vote/total_votes)*100,3)
    # Updating the candidate dictionary
    # Candidate keys updated to include both vote count and candidate vote percentage as value
    candidates_dictionary[row] = [candidates_dictionary[row], candidate_percentage]


# Set variable to represent the candidate name with the highest candidate vote count
# Using max function to determine the highest candidate vote in candidate dictionary
# Pull key associated with the highest candidate vote value
max_vote_candidate = max(candidates_dictionary, key = candidates_dictionary.get)

# Print commands to election result analysis
# Add output to print_result list for txt file printing
print(f"Election Results")
print_result.append(f"Election Results")
print(f"-------------------------")
print_result.append(f"-------------------------")
print(f"Total Votes: {total_votes}")
print_result.append(f"Total Votes: {total_votes}")
print(f"-------------------------")
print_result.append(f"-------------------------")

# For loop to perform percentage calculation based on unique candidate names
for row in candidate_list:
    # Applying the percentage calculation function referencing candidate dictionary
    percentage_calculation(candidates_dictionary[row])
    # printing the results to the percentage calculation
    print(f"{row}: {candidates_dictionary[row][1]}% ({candidates_dictionary[row][0]})")
    # Add output to print_result list for txt file printing
    print_result.append(f"{row}: {candidates_dictionary[row][1]}% ({candidates_dictionary[row][0]})")

# Print commands to election result analysis
# Add output to print_result list for txt file printing
print(f"-------------------------")
print_result.append(f"-------------------------")
print(f"Winner: {max_vote_candidate}")
print_result.append(f"Winner: {max_vote_candidate}")
print(f"-------------------------")
print_result.append(f"-------------------------")

# Creating output path for Results text file
output_path=os.path.join("Analysis","Result.txt")

# Printing output analysis results from list into a text file
with open(output_path,"w") as txtfile:
    for lines in print_result:
        txtfile.write(lines+"\n")
txtfile.close()
