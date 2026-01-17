from classes import Board, Animal

def checkAnimal(currentPlayer, animal):

    #If the animal is free
    if animal.owner is None:
        print(f"Animal: {animal.name}")
        print(f"Cost: {animal.cost}")
        choice = input("Do you want to buy this animal? (Y/N)")

        if choice.upper() == "Y":
            animal.setOwned(currentPlayer, animal)
        else:
            print("Animal not bought")

    # If the current player owns the animal
    elif animal.owner == currentPlayer:
        if animal.currentLevel < 3:
            choice = input("Do you want to upgrade this animal? (Y/N)")

