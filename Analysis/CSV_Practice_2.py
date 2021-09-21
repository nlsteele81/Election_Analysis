# # Add our dependencies.
import csv
import os
#dir(os)

# # Assign a variable to load a file from a path.
file_to_load = '/Users/nikki/Desktop/DataBootCamp/DataClasswork/Python/Election_Analysis/Analysis/election_results.csv'
#file_to_load = os.path.join("Analysis", "election_results.csv")

# # Open the election results and read the file.
with open(file_to_load) as election_data:

# # To do: perform analysis.

    #print(election_data)

# # To do: read and analyze the data here.
# # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
# # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)
    
# # Close the file.
#election_data.close()

# # Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
file_to_save = "/Users/nikki/Desktop/DataBootCamp/DataClasswork/Python/Election_Analysis/Analysis/election_analysis.txt"

# # Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#outfile = open("/Users/nikki/Desktop/DataBootCamp/DataClasswork/Python/Election_Analysis/Analysis/election_analysis.txt", "a")
#outfile = open(file_to_save, "w")

# # Write some data to the file.
#outfile.write("Hello World")

# # Close the file
#outfile.close()

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")
    
    # Write three counties to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")

    #txt_file.write("Arapahoe, Denver, Jefferson")
    
    #txt_file.write("Arapahoe\nDenver\nJefferson")

    # Skill Drill
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
