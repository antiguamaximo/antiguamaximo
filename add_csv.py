from csv import writer
new_info = ['Rampage', '1.03', '450','5','230']

with open('Information.csv','a') as file:
    writer_obj = writer(file)
    writer_obj.writerow(new_info)
    file.close()