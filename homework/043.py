n = int(input())
prime_factor = [1]
f=2
while n>1:
    if n%f==0:
        prime_factor.append(f)
        n//=f
    else:
        f+=1
print('*'.join(str(p) for p in prime_factor))
