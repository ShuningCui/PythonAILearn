string = input()
str1 = [string[i] for i in range(1,len(string)-1)]
str1.sort(reverse=True)
print(string[0]+''.join(str1)+string[-1])

