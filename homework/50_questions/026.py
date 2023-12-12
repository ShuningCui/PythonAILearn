num = [int(x) for x in input().split()]
num_out = [0]*len(num)
num.sort()
num_out[0]=num[0]
num_out[-1]=num[len(num)//2]
num_out[len(num)//2]=num[-1]
print(*num_out)
