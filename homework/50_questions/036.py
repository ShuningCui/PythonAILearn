string = input()
i = 0
while string[i]=='*':
    i += 1
j=len(string)-1
while string[j]=='*':
    j -= 1
print(string[i:j+1])