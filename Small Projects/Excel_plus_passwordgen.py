# Maximo Antigua    
#January, 2022

import random
import xlsxwriter
""""
FINISHED part of it. Now the password creator is class that asks for more information, stores it into the class and then whenever-
whenever its called the password gen updates a global  variable in the class with the information.
After all the information its input then an excel sheet funciton can be called to put all the information inside the dictionary -
into the sheet.
WHAT WILL BE NEXT?
- I could think of ways to improve the code. 
- Add an encryption method. 
- Request PIN to access? we will see
"""
class PasswordGen:
    information_forexcel = {}
    
    def __init__(self, website, username, passwordlength):
        self.website = website
        self.username = username
        self.passwordlength = passwordlength
        self.info = PasswordGen.information_forexcel
    
    def passwordgenerator(self):
        #Variables
        
        secured_password = ''
        characters = '1234567890abcdefghijklmnopqrstuvwxyz!@$&_-?%#;:<=>{]}()~ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        #checks length
        if self.passwordlength < 24:
            return print('Please the lenght should be longer than 24 characters.')
        #password creator
        for i in range(0, self.passwordlength):
            secured_password += random.choice(characters)
        return self.info.update({self.website: {'username/email': self.username, 'password': secured_password}})
    
    def information(self):
        return self.info
    
    def excel_workbook_creation(self):
        #This creates an excel document & adds a sheet (default to Sheet1)
        workbook = xlsxwriter.Workbook('Passwords.xlsx')
        worksheet = workbook.add_worksheet()
        #Bold format
        bold = workbook.add_format({'bold': 1})
        #This sets the location A1, B1, AND C1 to the assigned string provided .write format is: .write([location], [information], [format])
        worksheet.write('A1', 'WEBSITE', bold)
        worksheet.write('B1', 'USERNAME/EMAIL', bold)
        worksheet.write('C1', 'PASSWORD', bold)
        # Adjust the column width.
        worksheet.set_column(0, 0, 15)
        worksheet.set_column(2, 2, 15)
        worksheet.set_column(1, 1, 15)
        row=1
        col=0
        #iterates through the previously created dictionary in passwordgenerator and it adds it into the excel sheet
        for website, data in self.info.items():
            worksheet.write_string(row,col, website)
            worksheet.write_string(row, col+1, data['username/email'])
            worksheet.write_string(row, col+2, data['password'])
            row +=1
        workbook.close()


habbo = PasswordGen('habbo.com', 'maximoa10', 32)
capitalone = PasswordGen('Capitalone.com', 'MaximoA10', 24)
chase =  PasswordGen('chase.com', 'maximoantigua2', 32)


# habbo.passwordgenerator()
# capitalone.passwordgenerator()
# chase.passwordgenerator()

# chase.excel_workbook_creation()






