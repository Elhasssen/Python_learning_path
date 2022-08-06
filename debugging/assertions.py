import assertions


ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
# the assert function signals that the last item is 
# greater than the first one 
# so in the case of the .sort() function the program
# is bugfree
ages.reverse()
print(ages)
assert ages[0] <= ages[-1]
# when we assert that means we fail fast
# this will reduce the amount of code to check
# assertions are for programmers errors
# the user should never see an assertion failure
# when running scripts we use 
# python -0 myscript.py
# assertion are different from expetions because
# 

