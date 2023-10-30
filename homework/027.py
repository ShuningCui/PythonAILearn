n = int(input())*3
max = [s for s in str(n)]
max.sort(reverse=True)
print(n,''.join(max))
