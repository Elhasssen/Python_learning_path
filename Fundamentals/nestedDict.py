
allbuyers= {'Hassen' : {'apples': 6, 'bananas' : 3},
            'Nassir' : {'apples': 3, 'sodas' : 4},
            'Ismat'  : {'sodas' : 4, 'bread': 4}}

def totalbought(buyers, item):
    numBought = 0
    for k, v in buyers.items():
        numBought = numBought + v.get(item, 0)
    return numBought

print('Number of things being bought:')
print(' - Apples  ' + str(totalbought(allbuyers,'apples')))
print(' - sodas  ' + str(totalbought(allbuyers,'sodas')))
print(' - bananas  ' + str(totalbought(allbuyers,'bananas')))
print(' - bread  ' + str(totalbought(allbuyers,'bread')))
