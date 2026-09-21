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
screen.bgcolor("#d9fff6")

buttons = []
current_screen = "home"
knock_knock_lines = []
knock_knock_step = 0
bclr = "#8acbff"

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
    "Knock knock.\nWho's there?\nBen.\nBen who?\nBen knocking on the door all afternoon!",
    "Knock knock.\nWho's there?\nPasture.\nPasture who?\nPasture bed time, isn't it?",
    "Knock knock.\nWho's there?\nLena.\nLena who?\nLena little closer and I'll tell you.",
    "Knock knock.\nWho's there?\nEwan.\nEwan who?\nIt's just me.",
    "Knock knock.\nWho's there?\nNobel.\nNobel who?\nNobel, that's why I knocked!",
    "Knock knock.\nWho's there?\nNuisance.\nNuisance who?\nWhat's nuisance yesterday?",
    "Knock knock.\nWho's there?\nCash.\nCash who?\nNo thanks, I prefer peanuts.",
    "Knock knock.\nWho's there?\nHugo.\nHugo who?\nHugo-ing to let me in or not?",
    "Knock knock.\nWho's there?\nDoris.\nDoris who?\nDoris locked, let me in!",
    "Knock knock.\nWho's there?\nAlison.\nAlison who?\nAlison to you after you listen to me.",
    "Knock knock.\nWho's there?\nKent.\nKent who?\nKent you tell who it is?",
    "Knock knock.\nWho's there?\nBen.\nBen who?\nBen knocking on the door all afternoon!",
    "Knock knock.\nWho's there?\nHavana.\nHavana who?\nHavana a wonderful time. Wish you were here!",
    "Knock knock.\nWho's there?\nOlive.\nOlive who?\nOlive you!",
    "Knock knock.\nWho's there?\nDinosaur.\nDinosaur who?\nDinosaur because he fell down!",
    "Knock knock.\nWho's there?\nHarry.\nHarry who?\nHarry up and answer the door!",
    "Knock knock.\nWho's there?\nIce cream.\nIce cream who?\nIce cream every time I see a scary movie!",
    "Knock knock.\nWho's there?\nAdair.\nAdair who?\nAdair once, but now I'm bald.",
    "Knock knock.\nWho's there?\nHuron.\nHuron who?\nHuron my toe. Could you please get off it?",
    "Knock knock.\nWho's there?\nHawaii.\nHawaii who?\nI'm good. Hawaii you?",
    "Knock knock.\nWho's there?\nThumping.\nThumping who?\nThumping just just crawled up your leg.",
    "Knock knock.\nWho's there?\nAnnie.\nAnnie who?\nAnnie body home?",
    "Knock knock.\nWho's there?\nKenya.\nKenya who?\nKenya guess who it is?",
    "Knock knock.\nWho's there?\nD1.\nD1 who?\nD1 who knocked.",
    "Knock knock.\nWho's there?\nDistressing.\nDistressing who?\nDistressing has too much vinegar!",
    "Knock knock.\nWho's there?\nScold.\nScold who?\nScold out here!",
    "Knock knock.\nWho's there?\nWoo.\nWoo who?\nDon't get too excited--it's just a joke.",
    "Knock knock.\nWho's there?\nDewey.\nDewey who?\nDewey have to keep hearing all these jokes?",
    "Knock knock.\nWho's there?\nHowl.\nHowl who?\nHowl I get in if you don't open the door?",
    "Knock knock.\nWho's there?\nWaddle.\nWaddle who?\nWaddle I do if you don't open the door?",
    "Knock knock.\nWho's there?\nCook.\nCook who?\nHey! Who are you calling a cuckoo?",
    "Knock knock.\nWho's there?\nI won.\nI won who?\nI won to suck your blood.",
    "Knock knock.\nWho's there?\nSnow.\nSnow who?\nSnow time for questions. Just let me in!",
    "Knock knock.\nWho's there?\nTwig.\nTwig who?\nTwig or treat!",
]

TongueTwisterssay3x = [
    "Rolling red wagons race wildly down roads.",
    "Cooks cook cupcakes quickly.",
    "Jolly juggling jesters juggle jingle jacks.",
    "Nat the bat ate Pat the gnat.",
    "Quick kiss, quicker kiss.",
    "A moose noshes much mush.",
    "A proper copper coffee pot.",
    "Comical cactus curls rural wind.",
    "Six slippery snails slid slowly seaward.",
    "Patty pickes pretty papper packages.",
    "An ape hates grapes.",
    "A big black bug bit a big black bear.",
    "A tiny tiger thinks tough thoughts.",
    "Brenda's bunny baked buttered bread.",
    "Sly Sam slurps Sally's soup.",
    "See Sep slip.",
    "Are our oars oak?",
    "Susie sailed the seven seas.",
    "Which wristwatch is a Swiss wristwatch?",
    "Ten tricky two-toed turkeys trotted.",
    "She freed six sheep.",
    "She shouldn't shake the salt shakers, should she?",
    "Six silly sisters sort short socks.",
    "Girl gargoyle, guy gargoyle.",
    "Red bulb, blue bulb.",
    "Trained turtles trotted to the track.",
    "At eight Edgar ate eight eggs.",
    "Six smart sharks swam swiftly.",
    "Double bubble gum bubbles double.",
    "See me sneak in my squeaky, reeking sneakers.",
    "Two twins twirled twelve tires.",
    "If a black bug bleeds black blood, what color blood does a blue bug bleed?",
    "Sally saw Shelley singing swimming songs.",
    "I wish to wish the wish you wish to wish, but if you wish the wish the witch wishes, I won't wish the wish you wish to wish.",
    "Two totally tired toads tripped.",
    "Three free thoughtful seals.",
    "Six slick sight seers click.",
    "Six slippery snails slid slowly seaward.",
    "The ocean sure soaked Sherman.",
    "Katie's kittens caught Kyle's kite.",
    "Three free throws.",
    "A gazzillion gigantic grapes gushed gradually giving gophers gooey guts.",
    "Felix finds fresh french fries finer.",
    "Crisp crusts crakle and crunch.",
    "Roscoe rescued Rosie from the roaring rapids.",
]

Puns1text = [
    "Shoes are required to eat in the cafeteria. Socks can eat anyplace they want.",
    "I wondered why the baseball kept getting bigger. Then it hit me.",
    "I am reading a book about anti-gravity. It is impossible to put down.",
    "I only know 25 letters of the alphabet. I don't know y.",
    "Customer: Do you serve crabs?\nWaitress: Of course, sir. We serve anyone.",
    "Doctor: You need new glasses.\nPatient: How do you know? I haven't told you what's wrong with me yet.\nDoctor: I could tell as soon as you walked in through the window.",
    "Mother: Jay, let your brother have the sled half of the time!\nJay: I do, Mom. I have it going downhill and he has it going up."

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
        pen.goto(self.x, self.y - 13)

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
    buttons.append(Button(0, 70, 170, 40, "Tell Me a Joke",bclr, tell_random_joke))
    buttons.append(Button(0, 10, 170, 40, "Knock, Knock", bclr, tell_knock_knock))
    #buttons.append(Button(0, -290, 120, 40, "Exit", "lightcoral", screen.bye()))
    buttons.append(Button(0,-110, 150, 40, "Q & A Jokes", bclr, tell_QA))
    buttons.append(Button(0, -50, 190, 40, "Tongue Twisters", bclr, tell_tongue_twister))
    buttons.append(Button(0, -170, 150, 40, "Puns", bclr, tell_pun))

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
    r.choice([tell_QA, tell_knock_knock, tell_tongue_twister, tell_pun])()

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

def tell_tongue_twister():
    global current_screen
    current_screen = "tongue_twister"
    pen.clear()
    pen.hideturtle()
    pen.speed(0)

    index = r.randint(0, len(TongueTwisterssay3x) - 1)
    draw_joke(TongueTwisterssay3x[index], "")
    pen.pu()
    pen.goto(0, 180)
    pen.write("Say it 3 times fast!", align="center", font=("Arial", 16, "bold"))

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
    screen.update()

def tell_pun():
    global current_screen
    current_screen = "pun"
    pen.clear()
    pen.hideturtle()
    pen.speed(0)

    pun = r.choice(Puns1text)
    draw_joke(pun, "")

    pen.penup()
    pen.goto(0, -180)
    pen.write("Click anywhere for the home screen", align="center", font=("Arial", 14, "normal"))
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

    screen.update()

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