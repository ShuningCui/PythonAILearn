def is_laepyear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def get_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif is_laepyear(year):
        return 29
    else:
        return 28

input = [int(x) for x in input().split(',')]
print(get_days(input[0], input[1]))