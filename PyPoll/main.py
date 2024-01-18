#getting modules
import os
import csv

#csvpath = os.path.join('Resources', 'budget_data.csv')  
csvpath = os.path.join('Desktop','python_challenge','PyPoll','Resources','election_data.csv')

#open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #create lists to store data
    voter_id = []
    county = []
    candidate = []
    candidate_list = []
    candidate_votes = []
    candidate_percent = []
    candidate_count = []
    candidate_dict = {}
    winner = []

    #loop through csv file
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #count total votes
    total_votes = len(voter_id)

    #create list of candidates
    for name in candidate:
        if name not in candidate_list:
            candidate_list.append(name)

    #count votes for each candidate
    for name in candidate_list:
        candidate_votes.append(candidate.count(name))

    #calculate percentage of votes for each candidate
    for votes in candidate_votes:
        candidate_percent.append(round((votes/total_votes)*100,3))

    #create dictionary of candidates and votes
    candidate_dict = dict(zip(candidate_list,candidate_votes))

    #find winner
    winner = max(candidate_dict, key=candidate_dict.get)

    #print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {candidate_percent[i]}% ({candidate_votes[i]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #write results to text file
    output_path = os.path.join('Desktop','python_challenge','PyPoll','Resources','election_results.txt')
    with open(output_path, 'w') as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Total Votes: {total_votes}\n")
        txtfile.write("-------------------------\n")
        for i in range(len(candidate_list)):
            txtfile.write(f"{candidate_list[i]}: {candidate_percent[i]}% ({candidate_votes[i]})\n")
        txtfile.write("-------------------------\n")
        txtfile.write(f"Winner: {winner}\n")
        txtfile.write("-------------------------\n")