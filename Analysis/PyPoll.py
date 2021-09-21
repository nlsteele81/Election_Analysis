# # Add our dependencies.
import csv
import os
#dir(os)

# # Assign a variable to load a file from a path.
#file_to_load = '/Users/nikki/Desktop/DataBootCamp/DataClasswork/Python/Election_Analysis/Analysis/election_results.csv'
#file_to_load = os.path.join("Analysis", "election_results.csv")
file_to_load = "../Resources/election_results.csv"

# # Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
#file_to_save = "/Users/nikki/Desktop/DataBootCamp/DataClasswork/Python/Election_Analysis/Analysis/election_analysis.txt"
file_to_save = "election_analysis.txt"

# 1. Initialize a total vote counter.
total_votes = 0

# Declare a new list of candidate options.
candidate_options = []

# Declare an empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# # Open the election results and read the file.
with open(file_to_load) as election_data:

# # To do: perform analysis.

    #print(election_data)

# # To do: read and analyze the data here.
# # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# # Read and print the header row.
    headers = next(file_reader)
    #print(headers)
    
# # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        #candidate_options.append(candidate_name)

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: Print out the winning candidate, vote count and percentage to terminal.
        # Print each candidate, their vote count, and percentage to the terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print(candidate_results)

        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # 4. Print the candidate name and percentage of votes + Skill Drill.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage

            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

# 3. Print the total votes.
#print(total_votes)

# Print the candidate list.
#print(candidate_options)

# Print the candidate vote dictionary.
#print(candidate_votes)
    
# # Close the file.
#election_data.close()

