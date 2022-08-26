

num = '210'

digits = '0123456789'

index = 0

time = 0

for x in num:
    time += abs(digits.index(x) - index)
    index = digits.index(x)
    

print(time)