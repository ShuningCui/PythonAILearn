# 正整数n的因子m是任何小于或等于n且n能被m除尽的数。
# 例如，3是12的因子，因为12能够被3整除。
# 5不是12的因子，因为12除以5的余数是2。
# 用户输入一个正整数，然后打印出该数的因子。

n=int(input("pls input a integer"))
i = 1
while i<=n :
    if n%i == 0:
        print(i)
    i=i+1

