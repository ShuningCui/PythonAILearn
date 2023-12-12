input = [int(i) for i in input().split()]
isomorphic_number = []
for x in range(input[0], input[1] + 1):
    if str(x*x).endswith(str(x)):
        isomorphic_number.append(x)
print(*isomorphic_number)
