# The data we need to retrieve.

# add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Intialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_results:

    #to do: read and analyze the data here
    file_reader = csv.reader(election_results)

    # read the header row.
    headers = next(file_reader)

    #print each row in the CSV file.
    for row in file_reader:
        # 2. Add tot the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin Tracking theat candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1



# 3. Print the candidate votes dicitionary.
# 4. THe total number of votes each candidate won
#print(candidate_votes)

# 5. The winner of the election based on popular vote

# determine the percentage of votes for each candidate by looping through the counts.

# Iterate through the candidate list
for candidate_name in candidate_votes:
    # retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # print the candidate name and percentage of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name

#print winning candidate summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



# Print candidate's votes and percentages to .txt
#print(candidate_votes)

#txt_file.write(candidate_votes)

#using with statment open the file as a text file.
with open(file_to_save, "w") as txt_file:
 
    #write three countiees to the file.
    txt_file.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")

