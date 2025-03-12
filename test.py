x = [i for i in input().upper() if i.isalpha()]
y = []
for s in range(26):
    y.append((chr(ord('A')+s),x.count(chr(ord('A')+s))))
y.sort(key = lambda x:x[1],reverse = True)
z = [f'{t[0]}-{t[1]}' for t in y]
print(*z)