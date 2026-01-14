import random

# David is doing Animal()
class Animal:
    def __init__(self, name, cost, L0, L1, L2, L3, imageLink, setSquare): #cost = upgradecost
        self.name = name
        self.currentLevel = 0
        self.cost = cost
        self.L0 = L0
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3
        self.imageLink = imageLink # <-- we don't need this, we won't be rendering images - Adam
        self.setSquare = setSquare
        self.owned = False #? <-- whats wrong here? - Adam

    # you need to pass self as a parameter in these functions :D - Adam
    def getCost(self):
        return self.cost
    def upgrade(self, player):
        player.setMoney(player.getMoney() - self.cost)
        self.currentLevel += 1
    def getCurrentLevel(self):
        return self.currentLevel
    

# Adam is doing Player()
class Player(Animal):
    def __init__(self, name, boardPosition):
        self.playerID = random.randint(100,999)
        self.playerName = name
        self.boardPosition = boardPosition
        self.money = 0
        self.isOnOwnedSpace = False
        self.animals = [Animal("Lion", 100, False, False, False, False, False, 12)]

    def getPosition(self):
        return self.boardPosition
    
    def setPosition(self, position):
        self.boardPosition = position
    
    def getMoney(self):
        return self.money
    
    def setMoney(self, newMoney):
        self.boardPosition = newMoney
    
# Charlotte is doing Card()
class Card():
    def __init__(self, sentence, money):
        self.sentence = sentence
        self.money = money
    def get_sentence(self):
        return self.get_sentence
    def get_money(self):
        return self.get_money