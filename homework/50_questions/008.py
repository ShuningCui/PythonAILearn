n = list(input())
for i in range(len(n)):
    n[i] = str((int(n[i]) + 5) % 10)
n.reverse()
print(''.join(n))
