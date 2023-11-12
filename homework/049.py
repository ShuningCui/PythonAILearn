input = input().split()
str1 = input[0].upper()
str2 = input[1].upper()
str3 = []
for s in str1:
    if s not in str3:
        str3.append(s)
for s in str2:
    if s not in str3:
        str3.append(s)
str3.sort()
print(''.join(str3))
