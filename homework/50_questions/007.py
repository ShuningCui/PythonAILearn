n = int(input())
student_list = []
for i in range(n):
    student_list.append(input().split())
    student_list[i].append(sum([int(x) for x in student_list[i][-3:]]))
student_list.sort(key=lambda x: x[-1])
for student in student_list:
    print(*student)