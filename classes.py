import random

# Adam is doing Player()
class Player():
    def __init__(self, boardPosition, money=0):
        self.PlayerID = random.randint(100,999)
        self.boardPosition = boardPosition
        self.money = money

    def getPosition(self):
        return self.boardPosition
    
    def setPosition(self, position):
        self.boardPosition = position
    
    def getMoney(self):
        return self.money
    
    def setMoney(self, newMoney):
        self.boardPosition = newMoney
    


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
        self.imageLink = imageLink
        self.setSquare = setSquare
        self.owned = False #? <-- whats wrong here? - Adam

    # you need to pass self as a parameter in these functions :D - Adam
    def getCost():
        return self.cost
    def upgrade(player):
        player.setMoney(player.getMoney() - self.cost)
        self.currentLevel
    def getCurrentLevel():
        return self.currentLevel
    








# Charlotte is doing Card()
class Card():
    def __init__(self, sentence, money):
        self.sentence = sentence
        self.money = money
    def get_sentence(self):
        return self.get_sentence
    def get_money(self):
        return self.get_money