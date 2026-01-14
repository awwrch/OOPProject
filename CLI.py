# these are going to be printed in the terminal at some point to represent player cards, spaces, etc - will make more sense when done

class BoardComponents():
    def __init__(self, playerName, playerID, money):
        self.playerName = playerName
        self.playerID = playerID
        self.money = money

    @staticmethod # since we don't pass self
    def render_player_card(player):
        INNER_WIDTH = 36  # inside the box (between ║ ║)

        w = INNER_WIDTH
        lines = []

        lines.append("╔" + "═" * w + "╗")
        lines.append(f"║{'PLAYER CARD':^{w}}║")
        lines.append("╠" + "═" * w + "╣")

        lines.append(f"║ Name: {player.playerName:<{w - 7}}║")
        lines.append(f"║ 💰 Money: {player.money:<{w - 11}}║")
        lines.append(f"║ 📍 Board Pos: {player.boardPosition:<{w - 15}}║")

        lines.append("╠" + "═" * w + "╣")
        lines.append(f"║{'OWNED ANIMALS':^{w}}║")
        lines.append("╠" + "═" * w + "╣")

        if player.animals:
            for i, animal in enumerate(player.animals, 1):
                text = f"{i}. {animal.name} (Lv {animal.currentLevel})"
                lines.append(f"║ {text:<{w - 1}}║")
        else:
            lines.append(f"║ {'None':<{w}}║")

        lines.append("╚" + "═" * w + "╝")

        return "\n".join(lines)
