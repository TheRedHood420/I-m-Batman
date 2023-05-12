def main():
    print(f"The BATMAN")
    print(f"COMMISSIONER GORDON: Batman the riddle plans on detonating a atomic bomb, it's up to you stop him.")
    atts = reset()
    MENU = '''
\t|Menu|
S - Start
x - Save
Q - Quit
I - Investigate
P - Punch
B - Batarang
E - Explovises
R - Reset'''

    print(f"you've entered the warehouse, and are surrouded by an abyss darkness the only thing you can see is a small tape recorder.\n\nYou walk over and grab the tape recorder.")
def Level_One(Question):

    print(f"RIDDLER: Hello there dark knight, it's been a long while has it not. I presume You're here for my atomic bomb, I'm sorry but unfortunatley I cannot allow you to take it without a fight. So if you answer the riddle correctly you may enter. I'm guessing your silence means yes so let us begin")
    print(f"For six months the second boy wonder was dead until he came back.\n\nThis hero is known for his phrase. You must put your trust in me, Sirius star is the brighest star, Sally had a bad day, Dylan said he would come in 10 minutes, space is the darkest area, you should end your day with glory.\n\nWho am I?\n\n")
    Jason_Todd = input(Question)
    while Jason_Todd != "Green Lantern" and Jason_Todd != "I" and Jason_Todd != "i" and Jason_Todd != "P" and Jason_Todd != "p" and Jason_Todd != "B" and Jason_Todd != "b" and Jason_Todd != "E" and Jason_Todd != "e" and Jason_Todd != "()":
        Jason_Todd = Jason_Todd.title()
        if Jason_Todd == "Green Lantern":
            print(f"well done cape crusader.")
            return True
        elif Jason_Todd == "I" or "i":
            print(f"The room is almost pitch black")
        elif Jason_Todd == "P" or "p":
            print(f"Punching the air won't do anything")
        elif Jason_Todd == "B" or "b":
            print(f"You throw the batrang and hear it hit something but can't see it")
        elif Jason_Todd == "E" or "e":
            print(f"nothing happens")
            print(f"RIDDLER: Why?")
        else: 
            return False

def Level_two(Option,One,Two,Three):
    print("You enter through the door, The room looks almost reminiscent of a study. On the right side you see a large desk with some papers and pens on the desk. On the left side You see a large painting of the Joker riding a horse almost reminiscent of The Napoleon Crossing The Alps. on the right side of the room we see a large bookshelf. And directly in the middle of the room we see a table with three separate files and a vase of flowers.")
    print("welcome to your next trap... I'm mean room. mwhahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha\n now if you look at the desk you'll find 3 envelope pick one of the three and well good luck")
    Nightwing = 0
    Nightwing =  input(Option)
   
    while 1 > Nightwing or Nightwing > 3:
        Nightwing_is_int = False
        try: 
            Nightwing = int(Nightwing)
            Nightwing_is_int = True
        except: 
            print("Uh Bats thats not a number.")
            Nightwing = 0
        if(Nightwing_is_int):
            if 1 > Nightwing or Nightwing > 3:
                print("its just one of the three, batman.")
                one = "1"
            elif 1 == Nightwing:
                print("One may call it an insult, some may call it flattery, all the same it's a fun movie genre.")
                Two_Face = ""
                Two_Face = input("What am I?\n")
                Two_Face = Two_Face.lower()
                if Two_Face == "parody":
                    Two_Face = True
                    return One
                else:
                    return False
            elif 2 == Nightwing:
                print("Some WHAT has its thorns, Some WHAT are blue.")
                Harvey_Dent = ""
                Harvey_Dent = input("What am I?\n")
                Harvey_Dent = Harvey_Dent.lower()
                if Harvey_Dent == "flower" or Harvey == "flowers":
                    Harvey_Dent = True
                    return Two
                else: 
                    return False
            elif 3 == Nightwing:
                print("He had one of those rare smiles with quality of eternal reassurance in it, that you come across four or five times in life.")
                Penguin = ""
                Penguin = input("Who am I?\n")
                Penguin = Peiguin.lower()
                if Penguin == "gatsby": 
                    Penguin = true 
                    return Three
                else:
                    return False
            else:
                return False


def Level_two_Painting(One):
    print(f"RIDDLER: Well done cape crusader you figured out just 1 of many riddles, but now what must you do next, hurry the clock is ticking")
    while One != "the painting" and One != "painting" and One != "paint" and One != "":
        One = input("Enter where you'd like to investigate:\n")
        One = One.lower()
        if One == "the painting" or "painting" or "paint":
           One = True
           return One 
        else:
            print("Not quite")
            return False

def Level_two_Painting_exit(One):
    exit = input("Good job but how will you get through")
    while exit != "I" and exit != "i" and exit != "B" and exit != "b" and exit != "P" and exit != "p" and exit != "E" and exit != "e":
        if exit == "I" or "i":
            print("you investigate the painting and see that theres nothing behind the painting")
            return One
        elif exit == "B" or "b":
            print("You throw a batarang, at the painting")
            return One
        elif exit == "P" or "p":
            print("You punch through the painting")
            return One
        elif exit == "E" or "e":
            print("You blow up the painting")
            print("RIDDLER: JEEZ OVERKILL MUCH!")
            return One
        else: 
            print("Invalid")


def Level_two_Flower(Two):
    print(f"RIDDLER: Well done cape crusader you figured out just 1 of many riddles, but now what must you do next, hurry the clock is ticking")
    while Mr.Freeze != "flower vase" and Mr.Freeze != "flower" and Mr.Freeze != "vase of flowers" and Mr.Freeze != "the vase of flower" and Mr.Freeze != "the flower vase" and Mr.Freeze != "":
        Mr.Freeze = input("Enter where you'd like to investigate:\n")
        Mr.Freeze = Mr.Freeze.lower()
        if Mr.Freeze == "flower vase" or "flower" or "vase of flower" or "the vase of flower" or "the flower vase":
            Mr.Freeze = True
            return Two

def Level_two_Flower_exit(Two):
    exit = input("What will you do now")
    while exit != "I" and exit != "i" and exit != "B" and exit != "b" and exit != "P" and exit != "p" and exit != "E" and exit != "e":
        if exit == "I" or "i":
            print("You look at the vase, after lifting the vase a secret passage opens")
            return Two
        elif exit == "B" or "b":
            print("Nothing happens")
        elif exit == "P" or "p":
            print("Nothing happens")
        elif exit == "E" or "e":
            print("The vase is thrown of the table, opening a secret passage ")
            print("RIDDLER: JEEZ OVERKILL MUCH!")
            return Two
        else:
            print("Invalid")

def Level_two_BookShelf(Three):
    print(f"RIDDLER: Well done cape crusader you figured out just 1 of many riddles, but now what must you do next, hurry the clock is ticking")
    while Hugo_Strange != "bookshelf" and Hugo_Strange != "the bookshelf" and Hugo_Strange != "":
        Hugo_Strange = input("Enter where you'd like to investigate:\n")
        Hugo_Strange = Hugo_Strange.lower()
        if Hugo_Strange == "bookshelf" or "the bookshelf":
            Hugo_Strange = True
            return Three

def Level_two_BookShelf_exit(Three):
    exit = input("Good job but how will you get through")   
    while exit != "I" and exit != "i" and exit != "B" and exit != "b" and exit != "P" and exit != "p" and exit != "E" and exit != "e":
        if exit == "I" or "i":
            print("There nothing behind the bookcase")
            return 
        elif exit == "B" or "b":
            print("Nothing happens")
        elif exit == "P" or "p":
            print("nothing happens")
        elif exit == "E" or "e":
            print("The bookshelf is gone")
            return Three
        else: 
            print("Invalid")

def Level_Three(One):
	Print(f"You walk through the painting and enter a long conference room, with a door at the very end of the room. You see 6 small holes in the wall.\nYou see 4 small long table put together to make 1 large long table, with 4 chairs on each side of the table and 2 chairs on each end.")
	print(f"RIDDLER: Well howdy there partner, oh wait wrong room.\nI mean Batman we need to discuss your performance, You've been seriously lacking and unfortunately your on thin ice, and one more screw up you're FIRED! well I guess three more screw ups if you know I mean.")
    print(f"RIDDLER: Alright enough with the trivialitys, I know all you care about are the riddles so lets make this easy:\n people often come to visit, but most often or not they eventully stay, all are welcome to stay from withered old men to small little children, unfortunatly if one come to visit you they will say a teary goodbye.")
    Joker = ""
    tries = 1 
    Joker = input("what am I?\n")
    Joker = Joker.lower()
    while Joker != cemetery and tries < 3:
        if Joker == "cemetery":
            print(f"RIDDLER: Impressive")
            print(f"The door unlocks and opens, you walk through door.")
        elif Joker == "I" or "i":
            print(f"You look around and see nothing to strange but you can smell gas")
        elif Joker == "p" or "p":
            print(f"You try to punch through the glass but it seems to reinforced.")
        elif Joker == "B" or "b":
            print(f"You try to throw a batarang through the glass but it seems to reinforced.")
        elif Joker == "E" or "e":
            print(f"The Room engulf in flames")
        tries += 2
        else:
            print("Fire starts to shoot out the holes.")
        tries += 1

    if tries < 3:
        return One
    else:
        return False
        

def Level_Three(Three):
    print(f"You walk through the large passage way and find yourself in a room that looks like a small western tavern, with a small bar with drinks on top. About six tables with three chairs at each table.")
	Print(f"\nRIDDLER: Well howdy there partner, yall aren't from around these parts are you, no I didn't think so. Well let me introduce you to are local sheriff")
	print(f"\nOut walk Deadshot, a hired gun.")
	print(f"\nRIDDLER: INTRODUCING SHERIF FLOYD LAWTON he's gonna watch you and if you get it wrong, well lets just say we handle things quite differently here, getting the wrong answer is punishiable by death.")
	print(f"\nRIDDLER: Okay time for the riddle The good is wrong, the bad is right, the truth will trap you, these are all true if you look at it through a mirror.\nwhat am I?")
	print(f"\nDEADSHOT: If you ask me he's missing a few screw loose.")
	Orphan = ""
	tries = 1
	Deadshot = 3
    E = reverse
	Orphan = input("RIDDLER: I HEARD THAT!")
	Orphan = Orphan.lower()
	while Orphan != reverse and tries < 3:
		if Orphan == "reverse":
			print(f"RIDDLER: Well done")
			print(f"\nDEADSHOT: Cool do I still get paid for this?")
			print(f"\nRIDDLER: Yes, just let him through.")
			print(f"\nDEADSHOT: Cool hey bats can you give me a ride after this.")
			print(f"\nBATMAN: Sure you want a ride to the hospital.")
			print(f"\nDEADSHOT: Never mind.")
        elif Orphan == "I" or "i":
            print(f"It seems Deadshot it gaurding the only exit")
        elif Orphan == "P" or "p":
            print(f"DEADSHOT: Hey watch it!")
        elif Orphan == "B" or "b":
            print(f"DEADSHOT: Hey watch it!")
        elif Orphan == "E" or "e":
            print(f"DEADSHOT: Holy crap, you go ahead I don't get paid enough for this.")
            print(f"RIDDLER: Hey get back here your not getting paid for this.")
            print(f"DEADSHOT: Cool I'd rather live.")
		else:
			print("DEADSHOT: you have {Deadshot -= 1} chances left.")
			tries += 1
		if tries < 3:
			return Three
		else:
            print(f"DEADSHOT: Sorry Bats")
			return False

def Level_Boss_Fight(One):
#BOSS FIGHT WITH MR.FREEZE
#USE POSSIBLE RANDOM SEQUENCE CONSICTING OF THROWING A BATARANG OR DODGING GO UNTIL THREE IN A ROW 
import random
    print(f"You enter in what seem to be a walk in freezer, with cow and pigs meat hanging on a hooks. Out walks Mr.Freeze.")
    print(f"\nRIDDLER: Batman you've met Professor Fries right well, as you may know his wife is sick and needs medical attention well I've decided to be genorous and give to him $4.7 million to fund his research and to well get rid of are little bat problem.")
    print(f"\nMR.FREEZE: Sorry Batman, but I must do whatever it takes to save my beloved Nora.")
    print(f"\nDodge his attacks while also trying to throw batarang at him.")
    print(f"\n\n B - Batarang\n\n D - Dodge")

def Level_Boss_Fight(Two):
#BOSS FIGHT WITH KILLER CROC
#USE RANDOM SEQUENCE OF JUST LEFT OR RIGHT GO FOR 2 OUT THREE TO PASS
import random
    print(f"You enter through the secret passage way and see a small bridge above a body of water.")
    print(f"\nRIDDLER: Welcome Batman, have you met my pet alligator?")
    print(f"\nKILLER CROC: Don't call me your pet!")
    print(f"\n Croc jumps back into the water.")
    print(f"\n Guess where Killer Croc will pop up on your left or right")
    print(f"\n\nR - Right\n\nL - Left")

def Level_Boss_Fight(Three):
#BOSS FIGHT WITH SCARWCROW add random sequance for scarecrow where player has to choose either to punch or block and gamble wether or not scarwcrow reels back or slashes
import random
    print(f"You enter through the secret passage way, and a dark room and see a tall figure")
    print(f"\nRIDDLER:Um Batman have you met scarecrow, you have cool fight him. jeez that guy give me the creeps")
    print(f"\nSCARECROW: BATMAN, Your DEAD!")
    print("\n\nP - Punch\n\nB - Block")

def Level_Four(One):
    print(f"You walk through the door and walk into a small apartment complex. all the sudden the turns and has the riddler talking like a news reporter")
    print(f"\nRIDDLER: And with Sports BatFamily win the game by 18 points, when player 15 through the ball to player 2 and ran a touchdown witch got them 9 points afterward they kicked a fieldgoal witch landed them 14 points")
    print(f"\nRIDDLER: You I know we may are issue but I do have a appreciation for your whole bat family especially that those wards you have")
    Question = input("who am I talking about")
    Question = Question.title()
    while Question != "Robin" or Question != "":
        if Question == "Robin":
            print("Well done caped crusader")
            Question = True
            return One
        else: 
            return False


def Level_Four(Two):
    print(f"You enter in what seems to be a classroom, with a chalkboard on the wall and four rows of desk")
    print(f"\nRIDDLER: Your almost there batman, After this its just you and me.")
    print(f"\nRIDDLER: just one last riddle.\n Now riddle me this Batman what reminds people of smore's, comes before jr and is a even 10")
    Question = input("who am I?")
    Question = Question.lower()
    while Question != "sophomore" or Question != "":
        if Question == "sophonore":
            print("RIDDLER: Well done Dark knight.")
            print("The door opens")
            Question = True
            return Two
        elif Question == "I" or "i":
            print("Theres only one exit")
        elif Question == "B" or "b":
            print("nothing happens")
        elif Question == "P" or "p":
            print("nothing happens")
        elif Question == "E" or "e":
            print("nothing happens")
            print(RIDDLER:seriously)
        else:
            print("Nope")


def Level_Four(Three):
    print("You rush into the next room and find your self in what looks like a convience store, you look through a window a notice that a recording of the outside is playing where its cycling from day to night in 5 seconds")
    print("\nRIDDLER: Batman I must ask if your not going to buy anything then your going to have to leave.\n okay fine you can stay, but only because I'm having too much fun with.")
    print(("\nOkay now this should easy for you, what is the one thing that Flash can't outrun, Hourman only need 1 hour of, And booster gold can travel in."))
    Question = input("what am I?")
    Question = Question.lower()
    while Question != "time" or Question != "":
        if Question == "time":
            print("RIDDLER: Your so close.")
            Question= True
            return Three
        elif Question == "I" or "i":
            print("All the food seems to be real")
        elif Question == "B" or "b":
            print("The Windows reinforced")
        elif Question == "P" or "p":
            print("The window is reinforced ")
        elif Question == "E" or "e":
            print("nothing happened")
        else:
            print("not quite")
             

def Level_Five(One):
    print("You enter the next room and find yourself surrounded by Batman merch, and posters.")
    print("RIDDLER: Welcome to the final room batman, I thought it would be fun if I did something special for you.")
    print("RIDDLER: Now time for are final riddle, Now Riddle me this Batman who's origin has always been described as being multiple choice, who was known for wearing a red hood, and who could not live without you?")
    Question = input("Who am I?")
    Question = Question.lower()
    while Question != "joker" or Question != "":
        if Question == "joker":
            print("Well done darkknight, now bring it on.")
            Question = True
            return One
        elif Question == "I" or "i":
            print("You nothing to strange")
        elif Question == "B" or "b":
            print("You threw it at a plushie")
        elif Question == "P" or "p":
            print("Nothing happened")
        elif Question == "E" or "e":
            print("Nothing happens")
        else:
            print("Not quite")

def Level_Five(Three):
    print("You enter the next room and found yourself in a room of mirror.")
    print("RIDDLER: Welcome to your final challege. I thought it be nice if I surrounded you by your favorite person.")
    print("RIDDLER: This is one is fun, riddle me this, What is at the beginning green lantern, the end of hawk man's wing, at the beginning of greatness, and at the end of conniving?)
    Question = input("What am I?") 
    Question = Question.lower()
    while Question != "g" or Question != "":
        if Question == "g"  
            print("Well done darkknight, now bring it on.")
            Question = True
            return One
        elif Question == "I" or "i":
            print("You nothing to strange")
        elif Question == "B" or "b":
            print("You threw it at a plushie")
        elif Question == "P" or "p":
            print("Nothing happened")
        elif Question == "E" or "e":
            print("Nothing happens")
        else:
            print("Not quite")

def Level_Final_Boss(One,Two,Three):