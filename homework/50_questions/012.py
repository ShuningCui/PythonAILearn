def ispalindrome(n):
    return str(n) == str(n)[::-1]

n = int(input())
ispalindrome_number = []
for i in range(1000, n+1):
    if ispalindrome(i):
        ispalindrome_number.append(i)
print(*ispalindrome_number)