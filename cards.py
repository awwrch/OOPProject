# Louise's stuff
# Please do the same as you did for animals by using the following structure
# Card(sentence, money)
# e.g: Card("An earthquake happens and you lose 20 coins!", 20)

from classes import Card

CARDS = [
    Card("Kangaroo / A kangaroo hops off with your wallet — lose 85.", -85),
    Card("Snake / 200 of your money was stolen by snakes!",-200),
    Card("Lion / A mighty lion inspires the crowd — collect 150!",+150),
    Card("Elephant / An elephant knocks over your cart — pay 90. ",-90),
    Card("Fox / A clever fox helps you find a hidden stash — gain 120!",+120),
    Card("Bear / A hungry bear raids your supplies — lose 70.",-70),
    Card("Wolf / A loyal wolf protects your property — collect 100!",+100),
    Card("Monkey / Mischievous monkeys make a mess — pay 60.",-60),
    Card("Eagle / An eagle swoops in with a shiny coin — gain 50!",+50),
    Card("Dolphin / Playful dolphins help you sell tickets — earn 130!",+130),
    Card("Turtle / A slow turtle delays your delivery — lose 40."-40),
    Card("Hawk / A hawk spots danger, saving you repairs — gain 80!",+80),
    Card("Rabbit / A rabbit chews through your wiring — pay 45.",-45),
    Card("Boar / A wild boar charges through your fence — lose 75.",-75),
    Card("Owl / A wise owl guides you to a great deal — collect 110!",+100),
    Card("Crab / A crab snips your bag open — lose 30.",-30),
    Card("Horse / A strong horse helps haul materials — gain 140!",+140),
    Card("Penguin / A penguin parade boosts tourism — collect 95!",+95),
    Card("Giraffe / A tall giraffe knocks over your sign — pay 50.",-50),
    Card("Crocodile / A crocodile guards the river crossing — save 100!",+100)    
]




def pickDeck(current_player):
    print(deck[head].text)
    current_player.money += deck[head].amount
    head += 1