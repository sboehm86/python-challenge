#main
#election_data.csv
#Columns: Voter ID, County, Candidate

#Total number of votes cast
#Complete List of Candidates who recieved votes
#The percentage of votes each candidate won
#The winner of the election based on popular vote
#Print to Terminal and export to a text file

#imports
import os
import csv
poll_data='Resources/election_data.csv'
poll_export="Analysis/election_analysis.txt"

total_votes=0
winning_candidate=""
winning_count=0 
candidates=[] #options
candidate_votes={}

with open (poll_data) as poll_data:
    reader=csv.DictReader(poll_data)

    for row in reader:
        total_votes=total_votes+1
        candidate_name=row["Candidate"]

        #add candidates to list if not in already...
        if candidate_name not in (candidates):
            candidates.append(candidate_name)
            candidate_votes[candidate_name]=0
        
        #...beging counting votes
        candidate_votes[candidate_name]=candidate_votes[candidate_name]+1

with open (poll_export, "w") as txt_file:

    #print vote count
    election_results=( f'----------\n'
                        f'Election Results\n'
                        f'----------\n'
                        f'Total Votes: {total_votes}\n'
                        f'----------\n'
                        )
    print(election_results)

    txt_file.write(election_results)

    for candidates in candidate_votes:
        #count and percent
        votes=candidate_votes.get(candidates)
        vote_percent= float(votes)/float(total_votes)*100

        #winning candidate
        if (votes>winning_count):
            winning_count= votes
            winning_candidate=candidates
        
        voter_output=f'{candidates}: {vote_percent: .2f}% ({votes})\n'
        print(voter_output)

        txt_file.write(voter_output)

    winning_candidate_sum=( f'----------\n'
                            f'Winner: {winning_candidate}!\n'
                            f'----------\n')

    print(winning_candidate_sum)
    txt_file.write(winning_candidate_sum)