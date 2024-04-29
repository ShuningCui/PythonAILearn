n = int(input())

a,b=2,1

sum=a/b

for i in range(n-1):

    a,b=a+b,a

    sum+=a/b

print(f'{sum:.4f}')