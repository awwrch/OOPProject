from classes import Animal, Card, Player
from CLI import BoardComponents
from animals import ANIMALS
from cards import CARDS
import random

# this is where a bunch of the terminal user interface logic will go
#testPlayer = Player("Adam", 12)

#print(BoardComponents.render_player_card(testPlayer))

#def createNewPlayer(name):
    

def diceRoll(player):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    if roll1 == roll2:
        pickDeck()
    rollSum = roll1 + roll2
    player.setPosition(player.getPosition() + rollSum)
    checkAnimal()
def getcurrAnimal(player):
    currentAnimal = next((animal for animal in ANIMALS if animal.setSquare == player.getPosition()), None)
