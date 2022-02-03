import csv
from hashlib import new


rows = open('Information.csv').read().split('\n')
newrows=[]
for row in rows:
    if row not in newrows:
        newrows.append(row)
f = open('Information.csv', 'w')
f.write('\n'.join(newrows))
f.close()