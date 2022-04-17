#pypol homework Written by David Brunik from module 3.


# Create a filename variable to a direct or indirect path to the file.
import csv
from itertools import count
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

#candidate options
Candidate_options = []

#declare the empty dictionary.
candidate_votes = {}

#create county options
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#vote turnout
county_turnout = ""
county_count = 0
county_percentage = 0

# Open the election results and read the file. with open function as eleciton data
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
    # add to total vote count.
        total_votes = total_votes + 1
      
        
         # Print the candidate name from each row.
        candidate_name = row[2]

        county_name = row[1]

        if candidate_name not in Candidate_options:
        # Add the candidate name to the candidate list.
            Candidate_options.append(candidate_name)
        #2 begin tracking that candidates vote count.
        candidate_votes[candidate_name] = 0
        #add to that candidates count
        candidate_votes[candidate_name] += 1

    if county_name not in county_options 



#determine the percentage of votes for each candidate by looping through the counts.
#1. iterate through the candy list.
for candidate_name in candidate_votes:
    #2 vote count of candidate
    votes = candidate_votes[candidate_name]
    #3. % of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #4 print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage}% of the vote")

    # Print the candidate list.
    print(Candidate_options)       

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)






print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


#1 the data we need to retrieve
#1the total number of votes cast
#2 A complete list of candidates who received votes
#3 the percentage of votes each candidate won
#4 the total number of votes each candidate won
#5 The winner of the election based on popular vote