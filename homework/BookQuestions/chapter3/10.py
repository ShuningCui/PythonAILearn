# 10. 编写一个程序，寻找用户输入的几个整数中的最小值。
# 用户在1行内输入所有的整数。
# 例如：当用户输入数列为： 20 15 300 9 700时，
# 程序应该能够显示最小数是9。

input_nums = [int(x) for x in input("请输入几个整数：").split(' ')]
print(min(input_nums))