def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

input = [float(x) for x in input().split()]
if is_triangle(input[0], input[1], input[2]):
    print("YES")
else:
    print("ERROR DATA")

