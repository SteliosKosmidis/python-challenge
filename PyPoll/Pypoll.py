import csv

# Define the input file name
input_file = "../resources/election_data.csv"

# Define variables to store the calculated values
# Set up variables
total_votes = 0
Charles_Votes = 0
Diana_Votes= 0
Raymon_Votes=0
# Open the input file and read the data using the CSV module
with open(input_file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row

    # Loop through each row in the CSV file
    for row in csvreader:
 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1

        # We have four candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham": 
            Charles_Votes += 1
        elif row[2] == "Diana DeGette":
            Diana_Votes += 1
        elif row[2] == "Raymon Anthony Doane": 
            Raymon_Votes +=1
        

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Votes, Diana_Votes,Raymon_Votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
Charles_percent = (Charles_Votes/total_votes) *100
Diana_percent = (Diana_Votes/total_votes) * 100
Raymon_percent = (Raymon_Votes/total_votes)* 100


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_Votes})")
print(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_Votes})")
print(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_Votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

with open('poll_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Charles Casper Stockham: {Charles_percent:.3f}% ({Charles_Votes})\n")
    textfile.write(f"Diana DeGette: {Diana_percent:.3f}% ({Diana_Votes})\n")
    textfile.write(f"Raymon Anthony Doane: {Raymon_percent:.3f}% ({Raymon_Votes}))\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {key})\n")
    textfile.write("----------------------------\n")