import os
import csv
import sys

sys.stdout = open('solutions_pybank.txt' , 'w' )

#budget_info_csv = 'budget_data.csv'

#budget_info_csv = os.path.join('budget_data.csv')

with open("budget_data.csv",  newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)
    csv_header = next(csvreader)
    print(csv_header)


    csvreader_aslist =[]
    csvreader_aslist= list(csvreader)

    #print(csvreader_aslist)

    months=[]
    months = len(csvreader_aslist)
    print(months)

    print("Financial Analysis")
    print("----------------------------------------------------")
    print("Total number of months " + str(months))

    second_column =[]
    second_column = [row[1] for row in csvreader_aslist]
    #print(second_column)

    second_col_asint = []
    second_col_asint= list(map(int,second_column))
    #print(second_col_asint)

    total_sum = sum(second_col_asint)
    #print(total_sum)

    #print(second_col_asint)
    monthly_change=[]
    monthly_change = [second_col_asint[i]-second_col_asint[i+1] for i in  range(len(second_col_asint)-1)]
    #print(monthly_change)
   
    monthly_avg= sum(monthly_change)/(months-1)
    print("Average Monthly Change" + str(monthly_avg))

    max_val= max(second_col_asint)
    #print(max_val)
    print(second_col_asint.index(max_val))
    max_val_month = second_col_asint.index(max_val)
    print('Greatest Profit ' + str(csvreader_aslist[max_val_month]))

    min_val= min(second_col_asint)
    #print(min_val)
    print(second_col_asint.index(min_val))
    min_val_month = second_col_asint.index(min_val)    
    print('Greatest Loss ' + str(csvreader_aslist[min_val_month]))

    