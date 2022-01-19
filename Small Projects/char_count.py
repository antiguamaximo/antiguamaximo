
def duplicate_count(text):
    text = text.lower()
    counter = 0
    for i in text:
        if text.count(i) > 1:
            counter += 1
            text = text.replace(i, '')
        continue
    return counter

print(duplicate_count("abcdeaB"))
     