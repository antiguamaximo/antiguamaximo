#Maximo Antigua | Narcissistic Number January, 2022
"""""
What are the requirements?
1. Get a value.
2. Divide the value into its digits.
3. Set the digits to the power of the amount of digits & add them together (EJ: 153 = 3 digits, so [1^3 + 5^3 + 3^3]).
4. Check if the result of the addition is equal to the original value. (Example on #3, the addition its equal to its based value 153).
5. If it is equal, return TRUE. If not, it is not a narcissistic number and it should return FALSE.
"""""
def narcissistic(value):
    sum_of_val = 0
    for val in str(value):
        num = int(val)
        sum_of_val += num**len(str(value))
    if sum_of_val == value:
        return True
    else:
        return False
        

print(narcissistic(4887))
