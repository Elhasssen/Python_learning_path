def isPhoneNumber(text):
    # let's try this with Algerian phone number
    # ex: X-XXX-XXX-XXX
    if len(text) != 13 :
        return False
    if not text[0].isdecimal():
        return False
    if text[1] != '-':
        return False
    for i in range(2,5):
        if not text[i].isdecimal():
            return False
    if text[5] != '-':
        return False
    for i in range(6,9):
        if not text[i].isdecimal():
            return False
    if text[9] != '-' : 
        return False
    for i in range(10,13) : 
        if not text[i].isdecimal():
            return False
            
    return True

message = 'Call me at 0-789-543-666'
for i in range(len(message)):
    loaf = message[i:i+13]
    if isPhoneNumber(loaf):
        print('Phone number detected: ' + loaf)
