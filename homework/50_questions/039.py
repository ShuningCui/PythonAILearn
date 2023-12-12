total_seconds = int(input())
hours = total_seconds//3600
minutes = (total_seconds%3600)//60    
seconds = total_seconds%60
print(f'{hours}:{minutes:0>2}:{seconds:0>2}')
