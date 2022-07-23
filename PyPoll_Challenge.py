# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join('c:\\Users\\on080\\OneDrive\\Desktop\\Election Analysis\\Resources\\election_results.csv')
# Add a variable to save the file to a path.
file_to_save = os.path.join('c:\\Users\\on080\\OneDrive\\Desktop\\Election Analysis\\Analysis\\election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = [] 
candidate_votes = {}
#candidate_options = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
#candidate_votes = [209750048043.00, 1652373440459.00, 39145031540.00]
#candidate_dict = ({"Charles Casper Stockham": 209750048043.00, "Diana DeGette": 1652373440459.00,"Raymon Anthony Doane": 39145031540.00})

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
#county_options = ["Arapahoe", "Denver", "Jefferson"]
#county_votes = [111606705374.00, 1731451333819.00, 58210480849.00 ]
#county_dict = ({"Arapahoe": 111606705374.00,"Denver": 1731451333819.00,"Jefferson": 58210480849.00})

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
        # Read the header
        header = next(reader)

        # For each row in the CSV file.
        for row in reader:

                # Add to the total vote count
                total_votes = total_votes + 1

                # Get the candidate name from each row.
                candidate_name = row[2]

                # 3: Extract the county name from each row.
                county_name = row[1]

                # If the candidate does not match any existing candidate add it to the candidate list
                if candidate_name not in candidate_options:

                    # Add the candidate name to the candidate list.
                    candidate_options.append(candidate_name)

                    # And begin tracking that candidate's voter count.
                    candidate_votes[candidate_name] = 0

                # Add a vote to that candidate's count
                candidate_votes[candidate_name] += 1

                # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
                if county_name not in county_options:

                    # 4b: Add the existing county to the list of counties.
                    county_options.append(county_name)

                    # 4c: Begin tracking the county's vote count.
                    county_votes[county_name] = 0 

                # print('County Votes',county_votes.keys())
                county_votes[county_name] += 1

 # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
         f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes:\n"
        )
    
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_options in county_votes:
    
        # 6b: Retrieve the county vote 
        county_vote_count = county_votes[county_options]

        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(county_vote_count) / float(total_votes) * 100
    
        # 6d: Print the county results to the terminal.
        county_results = (f"{county_options}: {vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_results, end="")

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote_count > winning_county_count) and (vote_percentage > winning_county_percentage):
            winning_county_count = county_vote_count
            winning_county = county_options
            winning_county_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_turnout = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"Winning County Vote: {winning_county_count:,}\n"
    f"Winning County Percentage: {winning_county_percentage:.1f}%\n"
    f"-------------------------\n")
    
    print(largest_county_turnout)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_turnout) 
    name = "Diana DeGette"
    print(candidate_votes.get(name))

    # Save the final candidate vote count to the text file.
    #for candidate_name in candidate_votes:
    for key, value in candidate_votes.items(): 
        print(value) 
        # Retrieve vote count and percentage
        #votes = candidate_votes.get(candidate_name)
        votes = value 
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
        f"{key}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        candidate_votes = (f"\nCandidate Votes:\n")

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = key
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
