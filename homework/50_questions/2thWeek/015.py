# P015-判断任意一个正整数各位数字之和是奇数还是偶数
# 编程判断任意一个正整数各位数字之和是奇数还是偶数。
# 如果和是奇数输出1，偶数输出0。


num = [int(i) for i in input()]
print(int(sum(num)%2==1))