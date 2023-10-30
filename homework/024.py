string = [s for s in input().upper() if s.isalpha()]
count = []
for i in range(26):
    count.append((chr(65+i),string.count(chr(65+i))))
count.sort(key=lambda x:x[1],reverse=True)
out = [f'{s[0]}-{s[1]}' for s in count]
print(*out)