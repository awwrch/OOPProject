from classes import Animal, Card, Player
from CLI import BoardComponents

# this is where a bunch of the terminal user interface logic will go
# need to find something that works well/is easy to implement
testPlayer = Player("Adam", 12)

print(BoardComponents.render_player_card(testPlayer))