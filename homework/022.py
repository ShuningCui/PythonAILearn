num = [int(x) for x in input().split()]
count = 0
for i in range(num[0], num[1]+1):
    for j in range(i, num[1]+1):
        for k in range(j, num[1]+1):
            if i*i+j*j==k*k:
                count += 1
print(count)
