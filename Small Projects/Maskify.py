#Maximo Antigua | Maskify January, 2022
"""""
What are the requirements?
1. A string or value (name, cc number, etc) will be passed. Everything must change except the last 4 of the value passed.
2. Everyting except the last 4 should be changed for '####' signs.
3. It should return or print the new value for the user.
"""""

"""""
Now what should I do?
1. Collect the information. I should be able to iterate the whole value.
2. If its an integer I should change it to string, then iterate through it.
3. During the iteration, change everything but the last 4.
4. return a new string with the new values.
"""
def maskify(cc):
    
    #Checks if cc longer than 4 chars long. If not, it prints the current value.
    if len(cc) < 4:
        return print(cc)
    
    #Iterates through the cc without the last 4 values. Then replaces them with '#'
    counter = 0
    new_list = ''
    while len(cc[:-4]) > counter:
        new_list += '#'
        counter +=1

    return print(new_list+cc[-4:])
    