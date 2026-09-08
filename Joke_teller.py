# TODO types of jokes: knock-knock, pun, q and a, tongue twisters
# FUN write(e.g. "Home", move=False, align='left', font=(fontname, fontsize, fonttype))

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
knock_knock_lines = []
knock_knock_step = 0

# Jokes
Qjokes = [
    "Why did the scarecrow win an award?",#1
    "What do you call a fake noodle?",#2
    "What do you call a cow with a twitch?",#3
    "What do you get when you say \"tornado\" ten times forwards and backwards?",#4
    "How are two banana peels like shoes?",#5
    "What do you call a shy lamb?",#6
    "Why did cavemen draw pictures of hippopotamuses and rhinoceroses on their wall?",#7
    "On what nuts can pictures hang on?",#8
    "What do you call a bear with no teeth?",#9
    "What happens when 500 hares get loose in the center of town?",#10
    "What do you call a very popular perfume?",#11
    "What happens when a ghost gets lost in the fog?",#12
    "What do you call two spiders that just got married?",#13
    "What paces back and forth on the ocean floor?",#14
    "What goes thump, thump, thump, squish, thump, thump, thump, squish?",#15
    "When is a baseball player like a spider?",#16
    "What kind of a fish goes best with peanut butter?",#17
    "What did the beach say when the tide came in?",#18
    "What did the chewing gum say to the shoe?",#19
    "What goes zzub zzub?",#20
    "What is in an astronaut's favorite sandwich?",#21
]
Ajokes = [
    "Because he was outstanding in his field!",#1
    "An impasta!",#2
    "A milk shake!",#3
    "A real tongue twister!",#4
    "They're pair of slippers.",#5
    "Baaash-ful",#6
    "Because they couldn't spell the animals' names.",#7
    "Wall-nuts.",#8
    "A gummy bear!",#9
    "The police had to comb the area.",#10
    "A best-smeller.",#11
    "He is mist.",#12
    "Newlywebs.",#13
    "A nervous wreck.",#14
    "An elephant with one wet shoe.",#15
    "When he catches a fly.",#16
    "Jelly-fish.",#17
    "Long time, no sea.",#18
    "I'm stuck on you!",#19
    "A bee flying backwards.",#20
    "Lanuch meat!",#21
]

KnockKnockJokes = [
    "Knock knock.\nWho's there?\nLettuce.\nLettuce who?\nLettuce in, it's cold out here!",
    "Knock knock.\nWho's there?\nBoo.\nBoo who?\nAww why are you crying?",
    "Knock knock.\nWho's there?\nTank.\nTank who?\nYou're welcome!",
    "Knock knock.\nWho's there?\nCow go.\nCow go who?\nNo silly, cow go moooo!",
    "Knock knock.\nWho's there?\nHunch.\nHunch who?\nBless you!",
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
    buttons.append(Button(0, 70, 220, 60, "Tell Me a Joke", "lightblue", tell_random_joke))
    buttons.append(Button(-130, -50, 180, 60, "Knock, Knock", "lightgreen", tell_knock_knock))
    buttons.append(Button(0, -170, 120, 60, "Exit", "lightcoral", exit_app))
    buttons.append(Button(130,-50, 180, 60, "Q & A Jokes", "lightyellow", tell_QA))

    for button in buttons:
        button.draw()

    screen.update()


def tell_QA():
    global current_screen
    current_screen = "joke"
    pen.clear()
    pen.hideturtle()
    pen.speed(0)

    index = r.randint(0, len(Qjokes) - 1)
    draw_joke(Qjokes[index], Ajokes[index])


def tell_random_joke():
    r.choice([tell_QA, tell_knock_knock])()


def tell_knock_knock():
    global current_screen, knock_knock_lines, knock_knock_step
    current_screen = "knock_knock"
    pen.clear()
    pen.hideturtle()
    pen.speed(0)

    index = r.randint(0, len(KnockKnockJokes) - 1)
    knock_knock_lines = KnockKnockJokes[index].splitlines()
    knock_knock_step = 0
    show_knock_knock_line()


def show_knock_knock_line():
    pen.clear()
    pen.penup()
    pen.goto(0, 80)
    pen.color("black")
    pen.write(
        knock_knock_lines[knock_knock_step],
        align="center",
        font=("Arial", 24, "bold"),
    )

    pen.goto(0, -180)
    if knock_knock_step == len(knock_knock_lines) - 1:
        message = "Click anywhere to return home"
    else:
        message = "Click anywhere to continue"
    pen.write(message, align="center", font=("Arial", 14))
    screen.update()


def draw_joke(question, answer):
    lines = question.splitlines() + ["", answer]
    start_y = (len(lines) - 1) * 20 / 2

    pen.color("black")
    for line_number, line in enumerate(lines):
        pen.penup()
        pen.goto(0, start_y - line_number * 40)
        pen.write(
            line,
            align="center",
            font=("Arial", 20 if line_number == len(lines) - 1 else 18, "bold"),
        )

    pen.penup()
    pen.goto(0, -180)
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
    elif current_screen == "knock_knock":
        global knock_knock_step
        if knock_knock_step < len(knock_knock_lines) - 1:
            knock_knock_step += 1
            show_knock_knock_line()
        else:
            show_home_screen()
    else:
        show_home_screen()


screen.listen()
screen.onclick(handle_click)
show_home_screen()
screen.mainloop()