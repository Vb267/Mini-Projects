from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")
HIGHSCORE_FILE = "highscore.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("cyan")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 32, "bold"))
        self.reset_high_score_if_needed()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open(HIGHSCORE_FILE) as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def reset_high_score_if_needed(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGHSCORE_FILE, mode="w") as file:
                file.write(str(self.high_score))
