num = [int(x) for x in input().split()]
for i in range(num[0], num[1]+1):
    if i%7==0:
        print(f"{i} is a multiple of 7")
    if "7" in str(i):
        print(f"{i} contains 7")