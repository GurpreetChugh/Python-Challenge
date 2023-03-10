# This script is written in VS Code
import csv
from collections import Counter
# CSV file is in Resources folder in PyBank folder
file_path = r"PyPoll\Resources\election_data.csv"

with open(file_path, "r", encoding="utf-8") as csv_file:
    content = csv.reader(csv_file, delimiter=",")
     # Storing header
    header = next(content)
    
    # Creating tuples for each column Voter ID, County and Candidates and storing them under respective variables
    voter_id, county, candidates = zip(*list(content))
    

print("Election Results")
print("-"*25)
# # For a count of total number of votes cast we just need the total number of items in Voter ID tuple
total_vote = len(voter_id)
print(f"Total Votes: {total_vote}")
print("-"*25)

# # To calculate number and precentage of votes for each cxandidate we will make use of Counter class 
# # from collections module
candidate_count = Counter(candidates)

for key, value in candidate_count.items():
    print(f"{key}: {round((value/total_vote)*100, 2)}% ({value})")
    
print("-"*25)

# To find winner we just need the key with maximum value in candidate_count dict
winner = max(candidate_count, key= lambda k: candidate_count[k])
print(f"Winner: {winner}")

print("-"*25)

with open(r"PyPoll\Analysis\analysis.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-"*25 + "\n")
    txt_file.write(f"Total Votes: {total_vote}\n")
    txt_file.write("-"*25 + "\n")
    for key, value in candidate_count.items():
        txt_file.write(f"{key}: {round((value/total_vote)*100, 2)}% ({value})\n")        
    txt_file.write("-"*25 + "\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-"*25)
    
