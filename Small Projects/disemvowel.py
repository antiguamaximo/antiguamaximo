def disemvowel(string_):
    for v in 'aeiouAEIOU':
        string_ = string_.replace(v, '')
    return string_

print(disemvowel('This website is for losers LOL!'))
