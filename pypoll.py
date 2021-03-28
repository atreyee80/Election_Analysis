
import csv
import os

'''#Absolute file path
#Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
#file_to_load = os.path.join("Resources", "election_results.csv")
#with open(file_to_load) as election_source:
with open(file_to_load, 'r') as election_data:

    data = election_data.read()
    print(data)

file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
election_data = open(file_to_load,"r")
contents = election_data.read()
print(contents)
election_data.close()'''
#-------------------------------------------------------------------------------------------------------------------------
#Relative file path NOT DONE
'''file_to_load = "../Resources/election_results.csv"
fi = open(file_to_load,"r")
contents = fi.read()
print(contents)
fi.close()'''
#--------------------------------------------------------------------------------------------------------------------

### How to write to a file

# Assign a variable to save the file to a path.
'''file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    #Write some data to the file.
    txt_file.write("Arapahoe,")
    txt_file.write("Denver,")
    txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")'''

#---------------------------------------------------------------------------------------------------------------- 

# Read the file object with the reader function.
'''file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
election_data = open(file_to_load,"r")
file_reader = csv.reader(election_data)
# Print each row in the CSV file.
for row in file_reader:
    print(row)'''


#--------------------------------------------------------------------------------------------------------------------
'''# Add our dependencies to print the header row only
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)  '''
#-----------------------------------------------------------------------------------------------------------------------
'''#Total votes 
 
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'

# Initialize a total vote counter.
total_votes = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    #print(headers)
  
#Print each row in the CSV file.
    for row in file_reader:
            #print(row)
            print(row)
         # Add to the total vote count.
            total_votes =  total_votes + 1
         
       
            print(total_votes)'''
#----------------------------------------------------------------------------------------------------------------
'''# print the candidates names from each row
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'
# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)'''
#---------------------------------------------------------------------------------------------------------------------
'''# Print each candidate's name (unique name only  ) 
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'
# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

    
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

        
# Print the candidate list.
print(candidate_options)'''

#--------------------------------------------------------------------------------------------------------------
'''#Get The Candidate's votes

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'
# Initialize a total vote counter.
total_votes = 0

#Candidate votes and candidate option

#Declare the empty list for candidates
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

    
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

       #To increment each candidate's vote count every time their name appears in a row
        candidate_votes[candidate_name] += 1
        
# Print the candidate list.
print(candidate_votes) '''

#------------------------------------------------------------------------------------------------------------------------
#Calculate the percentage of votes received by each candidate's

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'
# Initialize a total vote counter.
total_votes = 0

#Candidate votes and candidate option

#Declare the empty list for candidates
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

    
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

       #To increment each candidate's vote count every time their name appears in a row
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
#--------------------------------------------------------------------------------------------------------------------
'''#Determine the Winning Candidate

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = '/Users/saha/Desktop/Resources1/Election_Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = '/Users/saha/Desktop/Resources1/Election_Analysis/analysis/election_analysis.txt'
# Initialize a total vote counter.
total_votes = 0

#Candidate votes and candidate option

#Declare the empty list for candidates
candidate_options = []
#Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

    
        # Add to the total vote count.
        total_votes += 1
      

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

       #To increment each candidate's vote count every time their name appears in a row
        candidate_votes[candidate_name] += 1

 # Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
    for candidate_name in candidate_votes:
    #  Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

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
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)'''
#--------------------------------------------------------------------------------------------------------------------
'''# Write the election_results to a text file

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)'''

#-------------------------------------------------------------------------------------
'''#Write the election results to a text file
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each candidate, their voter count, and percentage to the
    # terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
    # Print each candidate, their voter count, and percentage to the terminal.
    print(candidate_results)
   #Save the candidate results to our text file.
    txt_file.write(candidate_results)
    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
# Print the winning candidates' results to the terminal.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

#print(winning_candidate_summary)
# Print each candidate, their voter count, and percentage to the terminal.
#print(candidate_results)
#  Save the candidate results to our text file.
#txt_file.write(candidate_results)'''
#-------------------------------------------------------------------------------------
'''#Write the winning candidates results to  a text file
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)'''