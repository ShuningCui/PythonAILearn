string = input()
# Found the first character that is not a space
i = 0
while string[i] == " ":
    i += 1
# Found the last character that is not a space
j = len(string) - 1
while string[j] == " ":
    j -= 1
print(string[:i] + string[i:j+1].replace(" ", "") + string[j+1:])
