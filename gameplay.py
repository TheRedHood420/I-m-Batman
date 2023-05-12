class Game():
    def __init__(self, Riddle, answer): 
        self.Riddle = Riddle
        self.answer = answer
    def play(self):
        Batman = ""
        while Batman not in self.answer:
            print(self.Riddle)
            Batman = input("what am I?")
            Batman = Batman.lower()
            if Batman == self.answer:
                print ("well done")
        return Batman

    def Riddle_one(self):
        Riddle = ("For six months the second boy wonder was dead until he came back.\n\nThis hero is known for his phrase. You must put your trust in me, Sirius star is the brighest star, Sally had a bad day, Dylan said he would come in 10 minutes, space is the darkest area, you should end your day with glory.\n\nWho am I?\n\n")
        answer = ("green lantern")




    