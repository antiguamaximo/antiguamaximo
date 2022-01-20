#Maximo Antigua
#Random password creator
#                                         Good luck and happy coding :)!
""""
What do I want it to be?
- A password creator that will take a desired length and choose from simbols + letters + numbers to create a password.

How can I achieve this?
- I am still thinking about it but I'll need 3 different strings, strings with the alphabet(upper and lower), numbers and symbols.
- Should I applied OOP? or just have one big function? maybe apply the newly learned iterators? I am not sure.
- I'll need the random set? I forgot the word for it, and maybe itertools? If I decide to use iterators.
- Whatever I go with should give me a return password that (if i can make it happen) its of my desired lenght.
"""

## This is a modified version of the password_creator done before, but with more parameters and some adjustments.
import random

generated_password = {}

def generatePassword(website, username, lenght):
    secured_password = ''
    characters = '1234567890abcdefghijklmnopqrstuvwxyz!@$&_-?%#;:<=>{]}()~ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if lenght < 24:
        return print('Please the lenght should be longer than 24 characters.')
    
    for i in range(0, lenght):
        secured_password += random.choice(characters)
    generated_password.update({website: {'username/email': username, 'password': secured_password}})
    return 'Your new password is: {password}'.format(password=secured_password)

new_password = generatePassword('habbo.com', 'maxgab10', 24)
print(new_password)

print(generated_password)
        
    
    