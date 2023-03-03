# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 11:34:58 2023

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

val = df[df['Student_Number']==text_input].index.values
df.loc[val,"Student_Number"]

First_Name=df.loc[val,"First_Name"]
Last_Name=df.loc[val,"Last_Name"]
Student_Number=df.loc[val,"Student_Number"]
#DOB
df["DOB"] = pd.to_datetime(df["DOB"])
df["Date"] = df["DOB"].dt.date
DOB=df.loc[val,"Date"]
#END-DOB
Grade_Level=df.loc[val,"Grade_Level"]
Home_Room=df.loc[val,"Home_Room"]
Street=df.loc[val,"Street"]
City=df.loc[val,"City"]
State=df.loc[val,"State"]
Zip=df.loc[val,"Zip"]
Father=df.loc[val,"Father"]
Mother=df.loc[val,"Mother"]
