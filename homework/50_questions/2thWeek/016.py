# P016-求级数前n项的和
# 编程求以下级数前n项之和：
# s=1-1/3+1/5-1/7+1/9-1/11+1/13-1/15+.....
# 输入：一个正整数n
# 输出：前n项和的值，超出小数点后4位的，保留到小数点后4位


n = int(input())
sign, s = -1, 0
for i in range(n):
    sign *= -1
    s += sign * 1/(2*i+1)
print(round(s,4))