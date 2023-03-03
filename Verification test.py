# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:44:06 2023

@author: MAntigua
"""
import pandas as pd
import os
from docxtpl import DocxTemplate
import PySimpleGUI as sg
import datetime as dt

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

if df["Student_Number"].isin([int(text_input)]).any() == True:
    print("TRUE")
    

print(df["Student_Number"].isin([257343061]))

#print(df["Student_Number"].isin([int(text_input)]).index.values)

val = df[df['Student_Number']==int(text_input)].index.values

student_info = dict(df.loc[val])
#print(student_info)

for f in student_info.values():
    print(f)
#isin = int(text_input) in df['Student_Number'].tolist()
#print(f"User {text_input} is in file: {'yes' if isin else 'no'}")