num = [int(x) for x in input().split()]
count = [0,0,0,0,0]
for n in num:
    count[n] += 1
print(count)
