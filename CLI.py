# these are going to be printed in the terminal at some point to represent player cards, spaces, etc - will make more sense when done

class BoardComponents():
    def __init__(self, playerName, playerID, money):
        self.playerName = playerName
        self.playerID = playerID
        self.money = money

    @staticmethod # since we don't pass self
    def PlayerCard(player):
        return """"""