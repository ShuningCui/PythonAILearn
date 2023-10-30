num = int(input()) // 2
out = [chr(ord(s)+49) for s in str(num)]
print(num, ''.join(out))

