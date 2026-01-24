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
        TOTAL_SPACES = BOARD_SIZE + 1   # includes 0

        square_map = {i: [] for i in range(TOTAL_SPACES)}

        for idx, player in enumerate(players):
            pos = player.boardPosition % TOTAL_SPACES
            square_map[pos].append(idx)

        def tile(n):
            # no players → normal number
            if not square_map[n]:
                return f"{n:02d}"

            # one or more players → colour-stack
            out = ""
            for p in square_map[n]:
                out += f"{colours[p % len(colours)]}{n:02d}{RESET}"
            return out

        return f"""
    {tile(1)}──{tile(2)}──{tile(3)}──{tile(4)}──{tile(5)}──{tile(6)}──{tile(7)}
    │                        │
    {tile(26)}                      {tile(8)}
    │       {tile(13)}──{tile(14)}──{tile(15)}       │
    {tile(25)}       │       │      {tile(9)}
    │       {tile(12)}──{tile(11)}──{tile(16)}       │
    {tile(24)}                      {tile(10)}
    │                        │
    {tile(23)}──{tile(22)}──{tile(21)}──{tile(20)}──{tile(19)}──{tile(18)}──{tile(17)}
    """

    
    @staticmethod
    def choicePrompt(title, text_lines, choices, animal=None, width=60):
        top = "╔" + ("═" * width) + "╗"
        mid = "╠" + ("═" * width) + "╣"
        bottom = "╚" + ("═" * width) + "╝"

        result = ""

        result += top + "\n"
        result += "║  " + title.center(width - 4) + "  ║\n"
        result += mid + "\n"

        for line in text_lines:
            result += "║  " + line.ljust(width - 4) + "  ║\n"

        if animal is not None:
            result += mid + "\n"
            result += "║  " + f"Price: {animal.cost} coins".ljust(width - 4) + "  ║\n"
            result += "║  " + f"Charge: {animal.charge} coins".ljust(width - 4) + "  ║\n"

        result += mid + "\n"

        for i in range(len(choices)):
            result += "║  [" + str(i + 1) + "] " + choices[i].ljust(width - 8) + "  ║\n"

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
