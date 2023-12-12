string = input()
i = 0
while string[i]=='*':
    i += 1
print(string[i:]+string[:i])