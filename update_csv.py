import pandas as pd
import csv

#Method 1, knowing the location of the information that needs update
# df = pd.read_csv('Information.csv')

# df.loc[4, 'Username'] = 'xXRampageXx'

# df.to_csv('Information.csv', index=False)

# print(df)

#Method 2, using .replace() method. However, this changes a whole column of information
# df = pd.read_csv('Information.csv')
  
# # updating the column value/data
# df['Status'] = df['Status'].replace({'P': 'A'})
  
# # writing into the file
# df.to_csv('Information.csv', index=False)
  
# print(df)
#Method 3 Using CSV module
op = open("Information.csv", "r")
dt = csv.DictReader(op)
print(dt)
up_dt = []
for r in dt:
    print(r)
    row = {'Username': r['Username'],
           'KDR': r['KDR'],
           'Longest Shot': r['Longest Shot'],
           'Max Kills': r['Max Kills'],
           'Rounds Played': r['Rounds Played']}
    up_dt.append(row)
print(up_dt)
op.close()
op = open("Information.csv", "w", newline='')
headers = ['Username', 'KDR', 'Longest Shot', 'Max Kills', 'Rounds Played']
data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
data.writerow(dict((heads, heads) for heads in headers))
data.writerows(up_dt)
  
op.close()