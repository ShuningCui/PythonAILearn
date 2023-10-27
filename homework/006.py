n = int(input())
phone_list = []
for _ in range(n):
    phone_list.append(input())
phone_list.sort()
for phone in phone_list:
    print(phone)
