import csv  #get necessary module for reading csv files

#open file with election data
with open('./Resources/election_data.csv') as file:
    csvreader = csv.reader(file, delimiter = ",")

    vote_count = 0     #initialize vote count to 0
    Charles_Casper_Stockham = 0 #create variable for tracking candidate 1's votes
    Diana_DeGette = 0           #create variable for tracking candidate 2's votes
    Raymon_Anthony_Doane = 0    #create variable for tracking candidate 3's votes

    header = next(csvreader)     #store header row
    
    for row in csvreader:
        vote_count +=1 #count number of votes

        #increment vote count for candidate if their name is on this vote
        Charles_Casper_Stockham += row.count("Charles Casper Stockham")
        Diana_DeGette += row.count("Diana DeGette")
        Raymon_Anthony_Doane += row.count("Raymon Anthony Doane")

#calculate voting percentage of each candidate (vs the total vote)
Stockham_Percentage = Charles_Casper_Stockham/vote_count
DeGette_Percentage = Diana_DeGette/vote_count
Doane_Percentage = Raymon_Anthony_Doane/vote_count

#Determine the vote total that the winner received
Winner_Vote = max(Charles_Casper_Stockham,Diana_DeGette,Raymon_Anthony_Doane)

#Assign the winner of the election to the variable "Winner"
if Winner_Vote == Charles_Casper_Stockham:
    Winner = "Charles Casper Stockham"
elif Winner_Vote == Diana_DeGette:
    Winner = "Diana DeGette"
elif Winner_Vote == Raymon_Anthony_Doane:
    Winner = "Raymon Anthony Doane"

# Output results to screen
print("\nElection Results")
print("\n----------------------------")
print(f"\nTotal Votes: {vote_count}")
print("\n----------------------------")
print(f"\nCharles Casper Stockham {Stockham_Percentage:.3%} ({Charles_Casper_Stockham})")
print(f"\nDiana DeGette {DeGette_Percentage:.3%} ({Diana_DeGette})")
print(f"\nRaymon Anthony Doane {Doane_Percentage:.3%} ({Raymon_Anthony_Doane})")
print("\n----------------------------")
print(f"\nWinner: {Winner}")
print("\n----------------------------")

# Output same results to file
with open("./analysis/Voting Analysis.txt",'w') as file:
    file.write("\nElection Results")
    file.write("\n----------------------------")
    file.write(f"\nTotal Votes: {vote_count}")
    file.write("\n----------------------------")
    file.write(f"\nCharles Casper Stockham {Stockham_Percentage:.3%} ({Charles_Casper_Stockham})")
    file.write(f"\nDiana DeGette {DeGette_Percentage:.3%} ({Diana_DeGette})")
    file.write(f"\nRaymon Anthony Doane {Doane_Percentage:.3%} ({Raymon_Anthony_Doane})")
    file.write("\n----------------------------")
    file.write(f"\nWinner: {Winner}")
    file.write("\n----------------------------")