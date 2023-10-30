string = input().upper()
count = [0] * 26
for s in string:
    if s.isalpha():
        count[ord(s) - ord('A')] += 1
print(','.join([str(i) for i in count]))