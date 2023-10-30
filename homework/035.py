def encoder(x,n):
    if x.isupper():
        return chr((ord(x)-65+n)%26+65)
    elif x.islower():
        return chr((ord(x)-97+n)%26+97)

input_string = input().split()
string = input_string[0]
n = int(input_string[1])
print(''.join([encoder(x,n) for x in string if x.isalpha()]))