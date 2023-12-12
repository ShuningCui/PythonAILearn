def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

year = [int(x) for x in input().split()]
count = 0
while count<year[1]:
    if is_leap(year[0]):
        count += 1
    year[0] += 1
print(year[0]-1)