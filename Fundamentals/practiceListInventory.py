# write a function named display inventory that would
# take inventroy and diplay it like the following

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62


stuff = {'rope' : 1, 'torch' : 6,'gold coin' : 42, 
         'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
    print('Inventory : ')
    item_total = 0
    for k,v in inventory.items():
        item_total = item_total + v
        print(v,k)
    print('Toral number of items : ', item_total)

from charactercount import count

inv = {'gold coin' : 42, 'rope' : 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addtoinventorty(inventory, addeditems):
    
    Counteditems = count(addeditems)
    for k,v in Counteditems.items():
        if k in inventory:
            inventory[k] = inventory[k] + v
        else: 
            inventory[k] = v

    return inventory


inv = addtoinventorty(inv, dragonLoot) 
displayInventory(inv) 


    

    

        
        
    


