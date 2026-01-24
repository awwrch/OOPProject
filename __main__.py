from classes import Player
from CLI import BoardComponents
from animals import ANIMALS
from cards import CARDS
import random, os

deckPointer = 0  

def clear():
    os.system('cls')

def clearAndPlayerCard(player):
    os.system('cls')
    print(BoardComponents.render_player_card(player))

def findWinner(playerList):
    winner = playerList[0]

    for player in playerList:
        if getattr(player, "money") > getattr(winner, "money"):
            winner = player
    
    return winner

def checkAnimal(player):
    currentAnimal = next((animal for animal in ANIMALS if animal.setSquare == player.getPosition()), None)
    if currentAnimal.owned == False:
        print(BoardComponents.choicePrompt("Animal Purchase", [f"Do you want to buy {currentAnimal.name}?"], ["Buy", "Cancel"], currentAnimal))
        choice = int(input(f"Do you want to buy {currentAnimal.name}? ")) #ask if want buy(y/n)
        if choice == 1:
            currentAnimal.setOwned(player) #deducting and checking money is already within the function
            player.animals.append(currentAnimal)
        else:
            clear()
            print(f"You have not purchased {currentAnimal.name}")
            #output saying have not purchased
    elif currentAnimal.owned == True:
        if currentAnimal.owner == player.playerName:
            print(BoardComponents.choicePrompt("Upgrade Animal", ["Do you want to upgrade this animal?"], ["Upgrade", "Cancel"]))
            upgd = int(input(f"Do you want to upgrade {currentAnimal.name}? "))
            if upgd == 1:
                currentAnimal.upgrade(player)
            else:
                print(f"You have not upgraded {currentAnimal.name}.")
        else:
            actualOwner = fetchPlayerByName(currentAnimal.owner)            
            player.setMoney(player.getMoney() - currentAnimal.getAmountToCharge())
            actualOwner.setMoney(actualOwner.getMoney() + currentAnimal.getAmountToCharge())
            print(f"You have been charged {currentAnimal.getAmountToCharge()} coins")

def pickDeck(player):
    global deckPointer
    deck = CARDS.copy()
    current_card = deck[deckPointer]
    print(current_card.sentence)
    if current_card.minus:   
        player.money -= current_card.amount
    else:
        player.money += current_card.amount
    deckPointer += 1

def move(player):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    print(BoardComponents.dice())
    print(f"Dice 1: You rolled a {roll1}")
    print(f"Dice 2: You rolled a {roll2}")
    print(f"You move {roll1 + roll2} spaces")
    input("Press any key to continue...")
    if roll1 == roll2:
        print("You get a card!")
        clearAndPlayerCard(player)
        pickDeck(player)
    rollSum = roll1 + roll2
    player.setPosition(
        player.getPosition() + rollSum)
    if player.getPosition() > 25:
        player.setPosition(player.getPosition() - 26) #Assuming the board indexing has 0 for the square 'start'
        player.setMoney(player.getMoney() + 500)
    if player.getPosition != 0 and player.getPosition != 13: #checks that the player is not on special square
        clear()
        checkAnimal(player)
    elif player.getPosition == 13:
        print("You miss a turn!")
        player.toggleSkipTurn()

#main code vv
gameOn = True
playerList = []

print(
    BoardComponents.generalPrompt(
        "Player Count",
        [
            "How many people are playing",
        ],
    )
)
playerCount = int(input("> "))
clear()
for number in range(playerCount):      
    playerList.append(Player(number, ''))  #number becomes the playerid    try not to change this bit as my code is based entirely on the id
for i in range(len(playerList)):
    print(
    BoardComponents.generalPrompt(
        f"Player {i+1}: Choose name",
        [
            "Enter a name for your player",
        ],
    )
)
    playerList[i].playerName = str(input("> "))
    clear()
#maybe add code for printing players later

currentPlayerID = 0
def fetchPlayerByName(playerName):   #handy code for finding player by ID    for this to work names need to be unique
    player = next((player for player in playerList if player.playerName == playerName), None)  #may change this to find by name, and then using the player IDS only for turn indexing
    return player
clear()
print(BoardComponents.generalPrompt("Game Round Amount", ["How many rounds do you want to play?"]))
turns = int(input("> "))
clear()
print(BoardComponents.generalPrompt("Win Condition", ["How much money should a player need to win?"]))
winningAmount = int(input("> "))
while gameOn:
    for turn in range(turns):
        for player in playerList:
            if player.skipTurn == False:
                clearAndPlayerCard(player)
                print(BoardComponents.render_board(playerList))
                input("Press any key to roll...")
                clearAndPlayerCard(player)
                move(player)
            else:
                clearAndPlayerCard(player)
                print(BoardComponents.generalPrompt("Miss a turn!", [f"It's Player {player.playerID + 1}'s turn now!"]))
                player.toggleSkipTurn()
                continue
            if player.getMoney() >= winningAmount:
                winningPlayer = player.playerName()
                gameOn = False
                break
        if gameOn == False:
            break
    if gameOn:
        gameOn = False
        winningPlayer = findWinner(playerList)

print(f"Game over. {winningPlayer.playerName} has won.")