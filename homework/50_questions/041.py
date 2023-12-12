input = [float(x) for x in input().split(',')]
sum = input[0]*(1+input[2])**input[1]
print(f'{sum:.2f}')
