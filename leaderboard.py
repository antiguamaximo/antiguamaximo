import pandas as pd
#this function will return a leaderboard with the provided information given the filename and the name of the column. 
#NEEDS TO BE MODIFIED DEPENDING ON THE NAME OF THE ROWS!
def leaderboard(filename, stat):
    df = pd.read_csv(filename)

    #the part 'inplace=True' will not display the result of the document but it will apply the changes to the document.
    df1 = df.sort_values([stat], ascending=[False], inplace=True)

    #extracting columns after they were sorted 
    #Variables
    username = list(df['Username'])
    info = list(df[stat])
    ladder =f'```           Username  -     {stat}\n'
    counter =1

    #Crates a numbered leaderboard
    for n in range(0,5):
        ladder += f'''
        {counter}. {username[n]}   -  {info[n]}\n
        ```'''
        counter +=1
    return ladder

