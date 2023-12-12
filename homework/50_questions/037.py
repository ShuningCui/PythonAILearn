string_input = input().split()
string = string_input[0]
n = int(string_input[1])
i = len(string)-1
count = 0
while string[i]=='*':
    i -= 1
    count += 1
if count>n:
    print(string[:-(count-n)])
else:
    print(string)

