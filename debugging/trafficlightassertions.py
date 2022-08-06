
# ns = northsouth way ; ew = easrwest way
market_2nd = {'ns' : 'green', 'ew' : 'red'}
mission_16th = {'ns' : 'red', 'ew': 'green'}


def switchlight(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    # the asssert function signals to the function
    # that thee must be a red in the dictionnary
    # values
    assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)


switchlight(market_2nd)