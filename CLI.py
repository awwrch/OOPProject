# these are going to be printed in the terminal at some point to represent player cards, spaces, etc - will make more sense when done

class BoardComponents():
    def __init__(self, playerName, playerID, money):
        self.playerName = playerName
        self.playerID = playerID
        self.money = money

    @staticmethod # since we don't pass self
    def render_player_card(player):
        INNER_WIDTH = 36

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
            lines.append(f"║ {'None':<{w-1}}║")

        lines.append("╚" + "═" * w + "╝")

        return "\n".join(lines)
    

    @staticmethod
    def render_board(players):
        colours = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
        RESET = "\033[0m"
        BOARD_SIZE = 26

        square_map = {i: [] for i in range(1, BOARD_SIZE + 1)}

        for idx, player in enumerate(players):
            pos = player.boardPosition
            if pos <= 0:
                pos = 1
            elif pos > BOARD_SIZE:
                pos = ((pos - 1) % BOARD_SIZE) + 1
            square_map[pos].append(idx)

        def cell(n):
            if square_map[n]:
                s = ""
                for p in square_map[n]:
                    s += f"{colours[p % len(colours)]}{n:02d}{RESET}"
                return s
            return f"{n:02d}"

        return f"""
    [{cell(1)}]—[{cell(2)}]—[{cell(3)}]—[{cell(4)}]—[{cell(5)}]—[{cell(6)}]—[{cell(7)}]
    |                             |
    [{cell(26)}]                           [{cell(8)}]
    |        [{cell(12)}]—[{cell(13)}]           |
    [{cell(25)}]        |     |           [{cell(9)}]
    |        [{cell(14)}]—[{cell(15)}]           |
    [{cell(24)}]                           [{cell(10)}]
    |                             |
    [{cell(23)}]—[{cell(22)}]—[{cell(21)}]—[{cell(20)}]—[{cell(19)}]—[{cell(18)}]—[{cell(17)}]
    """
    
    @staticmethod
    def choicePrompt(title, text_lines, choices, width=60):
        top = "╔" + ("═" * width) + "╗"
        mid = "╠" + ("═" * width) + "╣"
        bottom = "╚" + ("═" * width) + "╝"

        result = ""

        result += top + "\n"
        result += "║  " + title.center(width - 4) + "  ║\n"
        result += mid + "\n"

        for line in text_lines:
            result += "║  " + line.ljust(width - 4) + "  ║\n"

        result += mid + "\n"

        for i in range(len(choices)):
            result += "║  [" + str(i+1) + "] " + choices[i].ljust(width - 8) + "  ║\n"

        result += bottom + "\n"

        return result
    
    @staticmethod
    def generalPrompt(title, text_lines):
        width = 60

        top = "╔" + ("═" * width) + "╗"
        mid = "╠" + ("═" * width) + "╣"
        bottom = "╚" + ("═" * width) + "╝"

        result = ""

        result += top + "\n"
        result += "║  " + title.center(width - 4) + "  ║\n"
        result += mid + "\n"

        for line in text_lines:
            result += "║  " + line.ljust(width - 4) + "  ║\n"

        result += bottom + "\n"

        return result
    
    @staticmethod
    def dice():
      return r"""
   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
        """
