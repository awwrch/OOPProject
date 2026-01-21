import random

# David is doing Animal()
class Animal:
    def __init__(self, name, cost, charge, setSquare):
        self.name = name
        self.currentLevel = 0
        self.cost = cost
        self.charge = charge
        self.setSquare = setSquare
        self.owned = False
        self.owner = None

    # you need to pass self as a parameter in these functions :D - Adam
    def getCost(self):
        return self.cost
    
    def upgrade(self, player):
        if player.getmoney() >= self.cost:
             player.setMoney(player.getMoney() - self.cost)
             self.currentLevel += 1
             print("Animal successfully upgraded")
        else:
            print("You don't have enough money")
            
    def getCurrentLevel(self, player):
        return self.currentLevel
    
    def setOwned(self, player):
        if player.getMoney() < self.cost:
            print("You don't have enough money")
        else:
            player.setMoney(player.getMoney() - self.cost)
            self.owned = True
            self.owner = player.playerName

    def getOwned(self):
         if self.owned == True:
            return self.owned
    def getAmountToCharge(self):
        multipliers = [1, 1.25, 1.5, 1.75]
        return self.charge * multipliers[self.currentLevel]

 
## Adam is doing Player()
class Player():
    def __init__(self, playerID, name):
        self.playerID = playerID
        self.playerName = name
        self.boardPosition = 0
        self.money = 2000
        self.isOnOwnedSpace = False
        self.animals = []
        self.skipTurn = False

    def getPosition(self):
        return self.boardPosition
    
    def setPosition(self, position):
        self.boardPosition = position
    
    def getMoney(self):
        return self.money
    
    def setMoney(self, newMoney):
        self.money = newMoney
    def toggleSkipTurn(self):
        self.skipTurn = not self.skipTurn
    
# Charlotte is doing Card()
class Card():
    def __init__(self, sentence, amount, minus):
        self.sentence = sentence
        self.amount = amount
        self.minus = minus
    def get_sentence(self):
        return self.get_sentence
    def get_money(self):
        return self.get_money