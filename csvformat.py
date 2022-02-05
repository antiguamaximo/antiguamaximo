
import csv
import os
import pandas as pd


#will be call to create a csv file provided the filename and fields. Should also provide PATH
def csvCreator(filename, fields, file_path, new_info):
    if os.path.isfile(file_path) == False:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
        with open(filename,'a') as file:
            writer_obj = csv.writer(file)
            writer_obj.writerow(new_info)   
#Will take as input a list with the information and the name of the csv file as a string. Everyting has to be on the same directory
def add_csv(new_info, csv_file):

    with open(csv_file,'a') as file:
        writer_obj = csv.writer(file)
        writer_obj.writerow(new_info)
        
#Takes as input the name of the csv file, creates a set to remove duplicates and then turns the information back into the document
def checkDup(csv_file):
    rows = open(csv_file).read().split('\n')
    newrows=[]
    for row in rows:
        if row not in newrows:
            newrows.append(row)
    f = open(csv_file, 'w')
    f.write('\n'.join(newrows))
    f.close()

# Takes a list, and filename as input and updates the information
def updateCsv(new_info, csv_file):

    op = open(csv_file, "r")
    dt = csv.DictReader(op)
    info = new_info
    up_dt = []

    for r in dt:
        row = {'Username': r['Username'],
            'KDR': r['KDR'],
            'Top 10s': r['Top 10s'],
            'Wins': r['Wins'],
            'Rounds Played': r['Rounds Played'],
            'Longest Shot': r['Longest Shot'],
            'Most Kills': r['Most Kills']}
        up_dt.append(row)

    op.close()
    for v in up_dt:
        if v['Username'] == info[0]:
            v['KDR'] = info[1]
            v['Top 10s'] = info[2]
            v['Wins'] = info[3]
            v['Rounds Played'] = info[4]
            v['Longest Shot'] = info[5]
            v['Most Kills']=info[6]

    op = open(csv_file, "w", newline='')
    headers = ['Username', 'KDR', 'Top 10s','Wins','Rounds Played', 'Longest Shot', 'Most Kills']
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    data.writerows(up_dt)
    op.close()

#for !set
def user_info(filename, fields, file_path, new_info):
    csvCreator(filename, fields, file_path, new_info)
    add_csv(new_info, filename)
    df = pd.read_csv(filename)
    df = df.drop_duplicates()
    df.to_csv(file_path)

#for !setdel
def del_user(filename, file_path, user):
    df = pd.read_csv(filename)
    df = df[df.Discord != user]
    df.to_csv(file_path)
    

    

