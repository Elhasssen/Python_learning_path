import logging
logging.basicConfig(level= logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

symbols = {1 : 'I', 4 : 'IV' , 5 : 'V' , 9 : 'IX' , 10 : 'X' , 40 : 'XL' , 50 : 'L' , 90 : 'XC' , 100 : 'C' , 400 : 'CD' , 500 : 'D' , 900 : 'CM' , 1000 : 'M'}
nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
romansym = []

number = int(input('Please enter an numbereger to translate\n'))
rem = number

for i in range(len(nums)):
    if rem in nums:
        romansym.append(symbols[rem])
        rem = 0
        break
    if rem > nums[i]:
        quo = rem // nums[i]
        rem = rem % nums[i]
        romansym.append(symbols[nums[i]]*quo)
        

print(''.join(romansym))