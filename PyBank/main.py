import os
import csv



#budget_info_csv = 'budget_data.csv'

budget_info_csv = os.path.join('budget_data.csv')

months =[]
revenue = []


with open(budget_info_csv,  newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    

    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))



#with open(budget_info_csv,') as budget_data:
 #   csvreader = csv.reader(budget_data, delimiter=',')

  #  print(csvreader)



    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



for row in csvreader:
        #print(row)
        months.append(row[0])


print(months)


#budget_info_df = pd.read_csv(budget_info_csv)
#budget_info_df.describe()

