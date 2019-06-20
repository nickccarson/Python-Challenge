import os
import csv
import sys

sys.stdout = open('solutions_pypoll.txt' , 'w' )

with open("election_data.csv",  newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    #print(csvreader)
    csv_header = next(csvreader)
    #print(csv_header)

    csvreader_aslist =[]
    csvreader_aslist= list(csvreader)

    print("ELECTION RESULTS")
    print("------------------------------")

    total_count_of_votes=[]
    total_count_of_votes= len(csvreader_aslist)
    print("TOTAL VOTES:   " + str(total_count_of_votes))  
    print("------------------------------")

    third_column =[]
    third_column = [row[2] for row in csvreader_aslist]


    # Python code to find unique elements- SET 
    candidate_set = [] 
    candidate_set = set(third_column)
    print("Candidates: " + str(candidate_set))
    candidate_list = []
    candidate_list = list(candidate_set)
print("------------------------------")

# find total number of votes per candidate
khan_count = []
khan_count= third_column.count("Khan")
#print(khan_count)
khan_percent_decimal = khan_count/total_count_of_votes
khan_percent = round( (khan_percent_decimal*100),3)
#print(khan_percent)

li_count = []
li_count= third_column.count("Li")
#print(li_count)
li_percent_decimal = li_count/total_count_of_votes
li_percent = round((li_percent_decimal*100),3)
#print(li_percent)

correy_count = []
correy_count = third_column.count("Correy")
#print(correy_count)
correy_percent_decimal = correy_count/total_count_of_votes
correy_percent = round((correy_percent_decimal*100),3)
#print(correy_percent)

otooley_count = []
otooley_count= third_column.count("O'Tooley")
#print(otooley_count)
otooley_percent_decimal = otooley_count/total_count_of_votes
otooley_percent= round((otooley_percent_decimal*100),3)
#print(otooley_percent)

print("Khan:    " + str(khan_percent) + "% Number of Votes: " + str(khan_count))
print("Correy:  "  + str(correy_percent) + "% Number of Votes: " + str(correy_count) ) 
print("Li:      " + str(li_percent) + "% Number of Votes: " + str(li_count))
print("O'Tooley: " + str(otooley_percent) + "%  Number of Votes: " + str(otooley_count) )

print("------------------------------")
print('Winner: Khan')
print("------------------------------")