num = [int(x) for x in input().split()]
daffodil = []
for i in range(num[0], num[1]+1):
    digit = [int(x)**3 for x in str(i)]
    if i==sum(digit):
        daffodil.append(i)
if len(daffodil)==0:
    print("-1")
else:
    print(*daffodil)