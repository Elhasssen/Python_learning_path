message = 'all i want to do in this life, is to learn everyday'



def count(message):
    count = {}
    for c in message:
    #this sets the character count at zero
        count.setdefault(c,0)
    #this will count
        count[c]=count[c]+1
    return  count



print(count(message))