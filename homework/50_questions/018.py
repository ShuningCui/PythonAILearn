num = [int(x) for x in input().split()]
series = [num[0]]
for i in range(1, num[1]):
    series.append(series[i-1]*10+num[0])
print('+'.join(str(s) for s in series)+"="+str(sum(series)))