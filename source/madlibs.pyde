
images = []
objects = ["Name: ", "Adjective: ", "Animal: ", "Day of the week: ", "Current tense Verb: ", "Verb 2: ", "Plural Noun: ", "Plural Animal: ", "Insturment: ", "Day of the week 2: ", "Day of the week 3: ", "Adjective 2: ", "Superhero: ", "Verb 3: ", "Adjective with 'est': ", "Complement: "]
phrases = ["YOOOOO!!!!", "STRAIGHT {1}!!!!", "IT'S {1} {2}\n{3}", "AM I STILL {4}?!?\n FRIDAY'S FINALLY HERE?", "I'M READY TO {5}\n THE DAY", "ME AND THE {6} FINNA\nEAT GOOD THIS MORNIN", "CMON WAKE UP BROSKI!!!", "I CANT WAIT TO SEE MY {7}", "{8} SOLO!!", "{9} AND {10}\nSURE WAS {11}...", "BUT TODAY IM FEELIN\nLIKE {12}!!!!", "WHEN THE OPPORTUNITY PRESENTS\nITS SELF I WILL\n{13} AT MY {14}", "MAN IM {15}!!!"]
times = [0, 2.5, 6.5, 9, 13.5, 17, 23, 26.5, 31, 34, 38.5, 43, 49.5, 59]
blanks = range(len(objects))

stage = "input"
question = 0
word = ""
slide = 0


def setup():
    global music, images, start_time, slide
    size(800, 600)
    for i in range(13):
        images.append(loadImage("fonky" + str(i) + ".jpg"))

def draw():
    global stage, images, slide, times, phrases, start_time
    
    background(22)
    textAlign(CENTER, CENTER)
    textSize(36)
    
    if stage == "input":
        text(objects[question], 400, 300)
        textSize(24)
        text(word, 400, 350)
        
    elif stage == "replace":
        for i in range(len(phrases)):
            while "{" in phrases[i]:
                index = int(phrases[i][phrases[i].find("{") + 1:phrases[i].find("}")])
                phrases[i] = phrases[i][0:phrases[i].find("{")] + str(blanks[index]) + phrases[i][phrases[i].find("}") + 1:len(phrases[i])]
        stage = "output"
        
    elif stage == "output":
        
        try:
            if millis() - start_time > times[(slide + 1)] * 1000 and slide < len(images):
                slide += 1
            image(images[slide], 0, 0, 800, 600)
            text(phrases[slide], 400, 500) 
        
        except IndexError:
            text("Thanks for watching", 400, 300)
        
        
def keyPressed():
    global word, question, stage, start_time
    
    if stage == "output":
        return
    
    if (keyCode >= 65 and keyCode <= 90) or keyCode == 32:
        word += chr(keyCode)
    
    elif key == BACKSPACE:
        if len(word) == 0 and question != 0:
            question -= 1
            word = blanks[question]
        else:
            word = word[0:len(word) - 1]
        
    elif key == ENTER or key == RETURN:
        blanks[question] = word
        if question < len(objects) - 1:
            question += 1
            word = ""
        else:
            start_time = millis()
            stage = "replace"
        
