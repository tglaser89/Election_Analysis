# The data we need to retrieve.

# add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_results:

    #to do: read and analyze the data here
    file_reader = csv.reader(election_results)

    # print the header row.
    headers = next(file_reader)
    print(headers)


#using with statment open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #write three countiees to the file.
    txt_file.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. THe total number of votes each candidate won
# 5. The winner of the election based on popular vote