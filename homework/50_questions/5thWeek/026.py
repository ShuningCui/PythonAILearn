# P026-按规则排序
# 编写程序，有一个包含奇数个项的整数序列，按照以下规则进行排序：
# 最大值排在中间，最小值排在最左，中值排在最右，其它值清为0。
# 输入n个数。
# 输出：排序后的数据，数据之间用空格分隔，最后一个数据后面没有空格。
# 样例1：
# 输入
# 66 10 30
# 输出
# 0 66 30
# 样例2：
# 输入
# 12 20 9 88 32
# 输出
# 9 0 88 0 20


num = [int(x) for x in input().split()]
num_out = [0]*len(num)
num.sort()
num_out[0]=num[0]
num_out[-1]=num[len(num)//2]
num_out[len(num)//2]=num[-1]
print(*num_out)
