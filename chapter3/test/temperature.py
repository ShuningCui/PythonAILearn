# Example
# 下面来编写一个名为temperature.py的脚本，定义两个函数:
# 1.	convert_cel_to_far()，它接受一个表示摄氏度的浮点参数，
# 并返回一个以华氏度表示相同温度的浮点数，使用以下公式:
# F = C * 9/5 + 32 
# 2. convert_far_to_cel()函数将华氏度转换为摄氏度，
# 使用以下公式: 
# C = (f - 32) * 5/9 
# 该脚本应该首先提示用户输入以华氏度为单位的温度，
# 然后显示转换为摄氏温度的温度。
# 然后提示用户输入以摄氏度为单位的温度，并显示转换为华氏度度的温度。
# 所有转换后的温度都应该四舍五入到小数点后两位。
def conver_cel_to_far(c):
    ''' 将华氏度转换为摄氏度'''
    return c * 9/5 + 32 
    

def conver_far_to_cel(f):
    c = (f - 32) * 5/9
    return c

c = float(input("请输入一个华氏温度值"))
f = round(conver_cel_to_far(c),2)
print(f)
# print(round(conver_cel_to_far(float
#    (input("请输入一个华氏温度值"))),2))


f = input("请输入一个摄氏温度")
f = float(f)
c = conver_far_to_cel(f)
print(round(c,2))
