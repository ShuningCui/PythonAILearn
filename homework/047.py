def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

input = [int(x) for x in input().split()]
count = 0
for i in range(input[0], input[1]-1):
    if is_prime(i) and is_prime(i+2):
        count += 1
print(count)
