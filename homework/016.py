n = int(input())
sign, s = -1, 0
for i in range(n):
    sign *= -1
    s += sign * 1/(2*i+1)
print(round(s,4))