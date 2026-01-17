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
        else:
            print("You don't have enough money")
            
    def getCurrentLevel(self, player):
        return self.currentLevel
    
    def setOwned(self, player):
        if player.getMoney() < self.cost:
            print("You don't have enough money")
        else:
            player.setMoney(player.getMoney() - self.cost)
        
    def getOwned(self):
         if self.owned == True:
            return self.owned
    def getAmountToCharge(self, charge):
        multipliers = [1, 1.25, 1.5, 1.75]
        return charge * multipliers[self.currentLevel]

 
## Adam is doing Player()
class Player():
    def __init__(self, name, boardPosition):
        self.playerID = random.randint(100,999)
        self.playerName = name
        self.boardPosition = boardPosition
        self.money = 0
        self.isOnOwnedSpace = False
        self.animals = [Animal("Lion", 100, 50, 3)] # test value, will be updated with a value for a list later on

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