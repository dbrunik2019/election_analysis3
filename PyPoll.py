#pypol homework


# Create a filename variable to a direct or indirect path to the file.
import os

file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")
outfile.write("Hello World")
outfile.close()

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties_in_the_election\n------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. initialize a total vote counter. 
total_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)


    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
    #2 add to total vote count.
        total_votes += 1
        print(total_votes)


#1 the data we need to retrieve
#1the total number of votes cast
#2 A complete list of candidates who received votes
#3 the percentage of votes each candidate won
#4 the total number of votes each candidate won
#5 The winner of the election based on popular vote