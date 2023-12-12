string = input()
count=i=start_index=0

while i < len(string)-1:
    count_current = 1
    start_index_current = i
    while i < len(string)-1 and string[i]==string[i+1]:
        count_current += 1
        i += 1
    if count_current > count:
        count = count_current
        start_index = start_index_current
    i += 1
print(string[start_index],count,start_index)