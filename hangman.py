from random import choice
import turtle

def initialScreen(draw,texting,yourScore,textX,textY,tries):
    texting.clear()
    draw.clear()

    draw.penup()
    draw.goto(-100,-300)
    draw.pendown()
    draw.goto(100,-300)
    draw.goto(100,300)
    draw.goto(-50,300)
    draw.goto(-50,200)

    texting.penup()
    texting.goto(textX,textY)
    texting.pendown()
    texting.color("purple")
    texting.write("Your score is {}".format(yourScore),font=("Calibri",10,"bold"))
    texting.color("black")
    texting.penup()
    texting.goto(textY,textY - 50)
    texting.pendown()

    return textY - 50

def drawHead(draw):
    draw.penup()
    draw.goto(-50,100)
    draw.pendown()
    draw.circle(50)

def drawBody(draw):
    draw.goto(-50,-100)
    draw.penup()
    draw.goto(-50,100)
    draw.pendown()

def drawRightHand(draw):
    draw.goto(-50,20)
    draw.goto(0,40)
    draw.penup()
    draw.goto(-50,100)
    draw.pendown()

def drawLeftHand(draw):
    draw.goto(-50,20)
    draw.goto(-100,40)
    draw.penup()
    draw.goto(-50,100)
    draw.pendown()

def drawRightLeg(draw):
    draw.goto(-50,-100)
    draw.goto(0,-180)
    draw.penup()
    draw.goto(-50,100)
    draw.pendown()

def drawLeftLeg(draw):
    draw.goto(-50,-100)
    draw.goto(-100,-180)
    draw.penup()
    draw.goto(-50,100)
    draw.pendown()

def checkEnd(out):
    End = True
    for letter in out:
        if letter == "_":
            End = False
            break
    return End


def drawHangman(texting,draw,mistakes,tries,textY):
    texting.write("Sorry wrong guess!",font=("Calibri",10,"bold"))
    textY -= 25
    texting.penup()
    texting.goto(textX,textY)
    texting.pendown()
    mistakes += 1
    tries -= 1
    if mistakes == 1:  drawHead(draw)
    elif mistakes == 2: drawBody(draw)
    elif mistakes == 3: drawRightHand(draw)
    elif mistakes == 4: drawLeftHand(draw)
    elif mistakes == 5: drawRightLeg(draw)
    elif mistakes == 6: drawLeftLeg(draw)
    return mistakes,tries,textY

def getGuess(word,found,out):
    while True:
        guess = turtle.textinput("Hello","Take your guess").lower()
        guess.strip()
        if guess != "":
            break
    for letter in range(len(word)):
        if word[letter] == guess:
            found = True
            out[letter] = guess
    return found , guess

def ending(yourScore,texting):
    TGREEN =  '\033[1;32m'
    TWHITE = '\033[m'
    yourScore += 1
    print(TGREEN + "You won! Your score is {}".format(yourScore) , TWHITE)
    texting.color("green")
    texting.write("You won!",font=("Calibri",15,"bold"))
    texting.color("black")
    return yourScore

def doCorrectProcess(texting,textX,textY):
    texting.write("Yeah right!",font=("Calibri",10,"bold"))
    textY -= 25
    texting.penup()
    texting.goto(textX,textY)
    texting.pendown()
    return textY

def outOfTries(word,texting,textX,textY):
    TGREEN =  '\033[5;31m'
    TWHITE = '\033[m'
    print (TGREEN + "You have lost baby! Correct answer was {}".format(word) , TWHITE)
    texting.color("red")
    textY -= 10
    texting.write("You lost!",font=("Calibri",15,"bold"))
    texting.color("black")
    texting.penup()
    texting.goto(textX - 50,textY-60)
    texting.pendown()
    texting.color("cyan")
    texting.write("Word was {}".format(word),font=("Calibri",20,"bold"))


def drawNumOfMistakes(mistake,tries):
    mistake.clear()
    mistake.penup()
    mistake.goto(textX,175)
    mistake.pendown()
    mistake.color("blue")
    mistake.write("You have {} chances!".format(tries),font=("Calibri",10,"bold"))

def yourword(yourWord,out):
    yourWord.color("orange")
    yourWord.clear()
    yourWord.penup()
    yourWord.goto(-350,0)
    yourWord.pendown()
    yourWord.write("  ".join(out),font=("Calibri",22,"bold"))

if __name__ == "__main__":
    sc = turtle.Screen()
    sc.title("Welcome to Hangman")
    draw , texting , mistake, yourWord = turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()
    draw.hideturtle()
    texting.hideturtle()
    mistake.hideturtle()
    yourWord.hideturtle()

    yourScore = 0
    while True:
        guesses = []
        tries , mistakes , textX , textY = 6 , 0 , 190 , 200
        word = choice(['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'desktop',
        'engineering', 'hangman', 'circuit', 'imagination', 'robot', 'memory', 'power', 'recursion',
        'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 'telephone',
        'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 'universe',
        'pyramid', 'sphere', 'member', 'warning', 'yourself', 'screen', 'language', 'elevator',
        'system', 'internet', 'parameter', 'traffic', 'network', 'filter', 'nucleus', 'result',
        'automatic', 'microphone', 'cassette', 'operation', 'country', 'beautiful', 'mission',
        'picture', 'teacher', 'superman', 'undertaker', 'alarm', 'process', 'keyboard', 'poetry',
        'electron', 'certificate', 'grandfather', 'landmark', 'relativity', 'eraser', 'amplifier',
        'design', 'football', 'human', 'musician', 'egyptian', 'elephant', 'queen', 'reception',
        'message', 'wallpaper', 'nationality', 'answer', 'wrong', 'statement', 'forest', 'dolphin',
        'puzzle', 'voltage', 'current', 'mathematics', 'wisdom', 'dream', 'supermarket', 'notebook',
        'database', 'collection', 'barrier', 'project', 'sunlight', 'figure', 'graph', 'orange',
        'battle', 'hundred', 'signal', 'thousand', 'transformation', 'daughter', 'flower', 'knife',
        'communication', 'microwave', 'electronic', 'peace', 'wireless', 'delete', 'window',
        'brain', 'control', 'prophet', 'freedom', 'harbour', 'confidence', 'positive', 'husband',
        'harvest', 'hunger', 'woman', 'children', 'stranger', 'garden', 'pleasure', 'laughter',
        'between', 'recognition', 'tomorrow', 'autumn', 'monkey', 'spring', 'winter', 'misfortune',
        'classification', 'typewriter', 'success', 'difference', 'acoustics', 'astronomy', 'train',
        'agreement', 'sorrow', 'christmas', 'silver', 'birthday', 'championship', 'friendship',
        'comfortable', 'diffusion', 'murder', 'policeman', 'science', 'desert', 'basketball',
        'blood', 'funeral', 'silence', 'garment', 'merchant', 'spirit', 'punishment', 'stone',
        'measurement', 'ocean', 'digital', 'illusion', 'tyrant', 'castle', 'passion', 'physician',
        'magician', 'remedy', 'knowledge', 'threshold', 'number', 'vision', 'expectation', 'fluid',
        'absence', 'mystery', 'morning', 'device', 'thoughts', 'spirit', 'future', 'impossible',
        'mountain', 'treasure', 'machine', 'whispering', 'eternity', 'reflection', 'occupation',
        'achievement', 'lightning', 'secret', 'environment', 'shepherd', 'confusion', 'expansion',
        'grave', 'promise', 'honour', 'reward', 'temple', 'distance', 'eagle', 'saturn', 'grass',
        'finger', 'belief', 'crystal', 'fashion', 'direction', 'captain', 'moment', 'improvement',
        'permission', 'logic', 'analysis', 'password', 'english', 'equalizer', 'simulation',
        'emotion', 'battle', 'expression', 'scissors', 'trousers', 'glasses', 'department', 'creation',
        'dictionary', 'chemistry', 'induction', 'detail', 'widow', 'wealth', 'health', 'faculty',
        'disaster', 'volcano', 'poverty', 'limitation', 'perfect', 'intelligence', 'infinite',
        'failure', 'ignorance', 'destination', 'source', 'resort', 'satisfaction', 'example', 'night',
        'frequency', 'selection', 'substitution', 'kingdom', 'pattern', 'management', 'experience',
        'situation', 'multiply', 'treatment', 'dollar', 'intuition', 'chapter', 'magnet', 'miracle',
        'desire', 'command', 'action', 'consciousness', 'enemy', 'security', 'object', 'realization',
        'happen', 'happiness', 'worry', 'method', 'tolerance', 'error', 'hesitation', 'register',
        'record', 'tongue', 'supply', 'vibration', 'stress', 'despair', 'restaurant', 'month', 'never',
        'television', 'video', 'audio', 'layer', 'mixture', 'doorbell', 'cousin', 'beard', 'corner']).lower()
        textY = initialScreen(draw,texting,yourScore,textX,textY,tries)
        out = ["_"] * len(word)
        while True:
            found = False
            yourword(yourWord,out)
            drawNumOfMistakes(mistake,tries)
            End = checkEnd(out)
            if End:
                yourScore = ending(yourScore,texting)
                break

            found , guess = getGuess(word,found,out)
            if guess in guesses:
                continue
            if len(guess) > 1 and len(guess) != len(word):
                continue
            if len(guess) == len(word):
                if guess == word:
                    out = word
                    textY = doCorrectProcess(texting,textX,textY)
                    yourScore = ending(yourScore,texting)
                    yourword(yourWord,out)
                    break                    
            guesses.append(guess)
            if not found: mistakes, tries, textY = drawHangman(texting,draw,mistakes,tries,textY)
            else: textY = doCorrectProcess(texting,textX,textY)

            if tries == 0:
                outOfTries(word,texting,textX,textY)
                break
        
        again = turtle.textinput("Hello","Do u want to play again? y/n").lower()
        if again == "n" or again == "no":
            break

        yourWord.clear()
        mistake.clear()
    print("Good luck!")