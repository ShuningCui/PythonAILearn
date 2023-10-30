num = [int(x)**2 for x in input().split()]
s = sum(num)
if s>=100:
    print(s//100)
else:
    print(s)
