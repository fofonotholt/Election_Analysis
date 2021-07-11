# Data we need to import.
#1. Get the total number of votes we need to cast.
#2. Create a list of candidateds that recieved votes.
#3. Get the total number of votes each canidate recieved.
#4. Percetange of votes each canidate recieved.
#5. The winner of the election by votes.

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)