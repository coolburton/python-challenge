import os
import csv

election_csv = os.path.join("election_data.csv")
output_txt = os.path.join("election_data_output.txt")

candidate = []
unique_candidate = []
vote_number = []
percent = []
percent_round = []

total_votes = 0


with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        candidate.append(row[2])
        candidate_name = row[2]
        if candidate_name not in unique_candidate:
            unique_candidate.append(candidate_name)
        
    for candidates in unique_candidate:
        vote_number.append(candidate.count(candidates))
        percent.append(round((candidate.count(candidates)/total_votes) * 100,3))
        

    winner = unique_candidate[vote_number.index(max(vote_number))]

    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------------")
    for i in range(len(unique_candidate)):
        print(f"{unique_candidate[i]}: {percent[i]}% ({vote_number[i]})")
    print("-------------------------------")
    print(f"Winner: {winner}")
    print("-------------------------------")

with open(output_txt, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------------\n")
    for i in range(len(unique_candidate)):
        txtfile.write(f"{unique_candidate[i]}: {percent[i]}% ({vote_number[i]})\n")
    txtfile.write("-------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------------\n")


    

        

     
        
                             


