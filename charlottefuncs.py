from classes import Board, Animal
from CLI import BoardComponents
from animals import ANIMALS

# the following code should handle the sale of an animal at a given square
# use the BoardComponents object, generalPrompt and choicePrompt to use the CLI and inputs below it
# 


def checkAnimal(player):
    currentAnimal = next((animal for animal in ANIMALS if animal.setSquare == player.getPosition()), None)
    if currentAnimal.owned == False:
        clear()
        print(BoardComponents.choicePrompt("Animal Purchase", [f"Do you want to buy {currentAnimal.name}?", "y/n"], ["Buy", "Cancel"]))
        choice = input(f"Do you want to buy {currentAnimal.name}? ").lower() #ask if want buy(y/n)
        if choice == 'yes' or choice == 'y':
            currentAnimal.setOwned(player) #deducting and checking money is already within the function
        else:
            clear()
            print(f"You have not purchased {currentAnimal.name}")
            #output saying have not purchased
    elif currentAnimal.owned == True:
        if currentAnimal.owner == player.playerName:
            print(BoardComponents.choicePrompt("Upgrade Animal", ["Do you want to upgrade this animal?", "y/n"], ["Upgrade", "Cancel"]))
            upgd = input(f"Do you want to upgrade {currentAnimal.name}? ").lower()
            if upgd == 'yes' or upgd == 'y':
                currentAnimal.upgrade(player)
            else:
                print(f"You have not upgraded {currentAnimal.name}.")
        else:
            actualOwner = fetchPlayerByName(currentAnimal.owner)            
            player.setMoney(player.getMoney() - currentAnimal.getAmountToCharge())
            actualOwner.setMoney(actualOwner.getMoney + currentAnimal.getAmountToCharge)
            print(f"You have been charged {currentAnimal.getAmountToCharge} coins")
               
#For the empty squares with no animals (start and miss a turn) I've set the return value when checking for the animal to None so use that as the parameter
#you also need to make function that deducts money from players that step on another player's animal

#The procedure checkAnimal:

#Takes the current player as a parameter
#Accesses the data for the animal at the player's position in the array board
#If the animal is free, asks the player if they would like to purchase the animal and outputs its name and cost, if
#they choose to buy the animal, it calls the procedure purchase() with the player and animal as parameters
#If that player owns the animal, and it is not at level 3, it asks if they would like to upgrade the animal
#If they would like to upgrade, it calls the method upgrade for that animal with the current player as a parameter
#If a different player owns the animal, it calls the method getAmountToCharge() for that animal, sending this value and the current player as parameters to the procedure chargeStay()
