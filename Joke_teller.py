 # TODO types of jokes: knock-knock, pun, q and a, tongue twisters
# FUN write(e.g. "Home", move=False, align='left', font=(fontname, fontsize, fonttype))
"""
Q. 2 "What do you call a shy lamb?" A. "Baaash-ful."
Q. 3 "Why did cavemen draw pictures of hippopotamuses and rhionceroses on their wall?" A. "Because they couldn't spell the animals\' names."
Q. 4 "On what nuts can pictures hang on?" A. "Wall-nuts."
Q. 5 "What happened when 500 hares get loose in the center of town?" A. "The police had to comb the area."
Q. 6 "What do you call a very popular perfume?" A. "A best-smeller."
Q. 7 "What do you call a polar bear wearing earmuffs?" A. "Anything you want. He can't hear you!"
Q. 8 "What happens when a ghost gets lost in the fog?" A. "He is mist."
Q. 9 "What do you call two spiders that just got married?" A. "Newlywebs."
Q. 10 "What paces back and forth on the ocean floor?" A. "A nervous wreck."
Q. 11 "What goes thump, thump, thump, squish, thump, thump, thump, squish?" A. "An elephant with one wet shoe."
Q. 12 "When is a baseball player like a spider?" A. "When he catches a fly."
Q. 13 "What kind of a fish goes best with peanut butter?" A. "Jelly-fish."
Q. """
# This is the start up
import turtle as t
import random as r

screen = t.Screen()
pen = t.Turtle()
screen.setup(width=1910, height=1000, startx=1, starty=1)
screen.title('Joke Teller')
screen.tracer(0)
pen.hideturtle()
pen.speed(0)

buttons = []
current_screen = "home"

# Jokes
Qjokes = [
    "Why did the scarecrow win an award?",#1
    "What do you call a fake noodle?",#2
    "What do you call a cow with a twitch?",#3
    "What do you get when you say \"tornado\" ten times forwards and backwards?",#4
    "How are two banana peels like shoes?",#5
]
Ajokes = [
    "Because he was outstanding in his field!",#1
    "An impasta!",#2
    "A milk shake!",#3
    "A real tongue twister!",#4
    "They're pair of slippers."#5
]


class Button:
    def __init__(self, x, y, width, height, text, color, callback):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.callback = callback

    def draw(self):
        pen.penup()
        pen.goto(self.x - self.width / 2, self.y + self.height / 2)
        pen.setheading(0)
        pen.pendown()
        pen.fillcolor(self.color)
        pen.begin_fill()
        for _ in range(2):
            pen.forward(self.width)
            pen.right(90)
            pen.forward(self.height)
            pen.right(90)
        pen.end_fill()
        pen.penup()
        pen.goto(self.x, self.y - 10)
        pen.color("black")
        pen.write(self.text, align="center", font=("Arial", 16, "bold"))

    def contains(self, x, y):
        return (
            self.x - self.width / 2 <= x <= self.x + self.width / 2
            and self.y - self.height / 2 <= y <= self.y + self.height / 2
        )


def show_home_screen():
    global current_screen
    current_screen = "home"
    pen.clear()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    pen.goto(0, 200)
    pen.color("black")
    pen.write("Joke Teller", align="center", font=("Arial", 60, "bold"))

    buttons.clear()
    buttons.append(Button(-150, -50, 220, 60, "Tell Me a Joke", "lightblue", tell_joke))
    buttons.append(Button(150, -50, 120, 60, "Exit", "lightcoral", exit_app))

    for button in buttons:
        button.draw()

    screen.update()


def tell_joke():
    global current_screen
    current_screen = "joke"
    pen.clear()
    pen.hideturtle()
    pen.speed(0)

    index = r.randint(0, len(Qjokes) - 1)

    pen.penup()
    pen.goto(0, 80)
    pen.color("black")
    pen.write(Qjokes[index], align="center", font=("Arial", 20, "bold"))

    pen.goto(0, 20)
    pen.write(Ajokes[index], align="center", font=("Arial", 18))

    pen.goto(0, -80)
    pen.write("Click anywhere to go back", align="center", font=("Arial", 14))

    screen.update()


def exit_app():
    screen.bye()


def handle_click(x, y):
    if current_screen == "home":
        for button in buttons:
            if button.contains(x, y):
                button.callback()
                return
    else:
        show_home_screen()


screen.listen()
screen.onclick(handle_click)
show_home_screen()
screen.mainloop()