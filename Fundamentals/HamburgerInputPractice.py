import pyinputplus as pyip

# First we declare the bread, protein, and cheese
# to calulate the price of served Sandwish
BreadPrice = {'Wheat': 10, 'White' : 15, 'Sourdough' : 20}
ProteinPrice = {'Chicken' : 10, 'Turkey' : 15, 'Ham' : 20, 'Tofu' : 25}
CheesePrice = {'Cheddar' : 10, 'Swiss' : 15, 'Mozzarella' : 20}
# first we ask what kind of break the client need
ResponseBread = pyip.inputMenu(['Wheat','White','Sourdough'] , prompt= 'What kind of bread do you like?\n')
# then we ask what kind of protein they want 
ResponseProtein = pyip.inputMenu(['Chicken','Turkey','Ham'], prompt= 'what type of protein do you want?\n')
# then we ask if the client want the cheese or not
DYWCheese = pyip.inputYesNo(prompt='Do you want cheese?\n')
# then we display the cheese menu 
ResponseCheese = pyip.inputMenu(['Cheddar','Swiss','Mozzarella'], prompt= 'What kind of cheese do you want?\n')
# the we ask of how many sandwhiches they want 
ResponseSandwich = pyip.inputInt(prompt= 'How Manysandwiches do you want?\n')
if ResponseSandwich > 0 :
    if DYWCheese == 'yes' :
        FullPrice = (BreadPrice[ResponseBread] + ProteinPrice[ResponseProtein] + CheesePrice[ResponseCheese]) * ResponseSandwich
    elif DYWCheese == 'no' :
        FullPrice = (BreadPrice[ResponseBread] + ProteinPrice[ResponseProtein]) * ResponseSandwich
    print('the full price is %s' % FullPrice)
        
