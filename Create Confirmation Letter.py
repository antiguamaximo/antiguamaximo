# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:12:45 2023

@author: MAntigua
"""
import pandas as pd
import os
from docxtpl import DocxTemplate
import PySimpleGUI as sg


#Enter the complete filepath to the Word Template
fname2=r"C:\Users\MAntigua\Desktop\Verification Letter\Verification_Letter_Template.docx"


#Enter the folder path to where you want to save the final word  files
os.chdir(r"C:\Users\MAntigua\Desktop\Verification Letter")


#Enter the complete filepath to the excel file which has the data
df=pd.read_excel(r"C:\Users\MAntigua\Desktop\Verification Letter\Student_info.xlsx")

#Create the window

sg.theme("DarkAmber")
layout = [[sg.Text('Input Student OSIS')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      
window = sg.Window('Student OSIS:', layout)    
event, values = window.read()    
window.close()
text_input = values[0]    


# End of Window

First_Name=df["First_Name"].values
Last_Name=df["Last_Name"].values
Student_Number=df["Student_Number"].values
#DOB
df["DOB"] =pd.to_datetime(df["DOB"])
df["Date"] = df["DOB"].dt.date
DOB=df["Date"].values
#END-DOB
Grade_Level=df["Grade_Level"].values
Home_Room=df["Home_Room"].values
Street=df["Street"].values
City=df["City"].values
State=df["State"].values
Zip=df["Zip"].values
Father=df["Father"].values
Mother=df["Mother"].values

# I was able to pull the index of a number provided by user
#And I was also able to display the osis by using that index and the name of column.


zipped=zip(First_Name,Last_Name,Mother,Father,Student_Number,DOB,Grade_Level,Home_Room,Street,City,State,Zip)

for a,b,c,d,e,f,g,h,i,j,k,l in zipped:


    doc=DocxTemplate(fname2)

    context={"First_Name":a,"Last_Name":b,"Mother":c,"Father":d,"Student_Number":e,"DOB":f,"Grade_Level":g,"Home_Room":h,"Street":i,"City":j,"State":k,"Zip":l}
    doc.rend()
    doc.render(context)
    doc.save(f'Verification Letter {First_Name} {Last_Name}.docx')
    print("Finished")
    
sg.popup('Files for OSIS', text_input, 'finished.')