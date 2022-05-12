input = "A 1 a"

if input.isalnum():
    print('"', input, '" : alnum')
else:
    print('"', input, '" is not alnum')

for word in input:
    if word.isupper():
        print("'", word, "' : uppercase")
    elif word.isspace():
        print("'", word, "' : space")
    elif word.isdigit():
        print("'", word, "' : number")
    elif word.islower():
        print("'", word, "' : lowercase")
