def collatzsequence(number):
    if number % 2 == 0 and number != 1: 
        a = number // 2
        print(a)
        collatzsequence(a)
    elif number % 2 == 1 and number != 1:
        b = number * 3 + 1
        print(b)
        collatzsequence(b)
    
collatzsequence(100)

# another program 
# while True:

#     x=int(input('ENTER NO.:'))
#     print ('----------------')
#     while x>0:
#         if x%2==0:
#             x = x/2
#         elif x>1:
#             x = 3*x + 1
#         else:
#             break
#         print(x)