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
            lines.append(f"║ {'None':<{w}}║")

        lines.append("╚" + "═" * w + "╝")

        return "\n".join(lines)
    
    def render_board(player):
      colourRED = "\033[31m"
      RESET = "\033[0m"
      boxes = []

      for i in range(1, 21):
          if i == player.boardPosition:
              boxes.append(f"{colourRED}{i:02d}{RESET}")
          else:
              boxes.append(f"{i:02d}")

      b = boxes

      return f"""\
  [{b[0]}]—[{b[1]}]—[{b[2]}]—[{b[3]}]—[{b[4]}]
    |                     |
  [{b[19]}]                 [{b[5]}]
    |                     |
  [{b[18]}]                 [{b[6]}]
    |                     |
  [{b[17]}]                 [{b[7]}]
    |                     |
  [{b[16]}]                 [{b[8]}]
    |                     |
  [{b[15]}]                 [{b[9]}]
    |                     |
  [{b[14]}]—[{b[13]}]—[{b[12]}]—[{b[11]}]—[{b[10]}]
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
