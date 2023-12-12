num = [int(x) for x in input()]
english = ['zero','one','two','three','four','five','six','seven','eight','nine']
out = [english[n] for n in num] 
print(*out)