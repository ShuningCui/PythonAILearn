string = input()
out = [string[-i:] for i in range(1, len(string)+1)]
print(*out)