def get_input(Riddle, answer):
    Batman = ""
    while Batman not in answer:
        print(Riddle)
        for x in answer:
            print(x)
        Batman = input("What am I?")
        Batman = Batman.lower()
    return Batman

class Inventory:
    def __init__(self, belt):
        self.belt = belt

    def storage(self):
        for belt in self.belt:
            print(belt + " " + str(self.belt[belt]))
    
    def add(self,item):
        if item in self.belt:
            self.belt[item] += 1
        else:
            self.belt[item] = 1

    def remove(self,item):
        if item in self.belt:
            self.belt[item] -= 1
            if self.belt[item] == 0:
                self.belt.pop(item)

utility = {
    "Batarang": 10,
    "Explosives": 10,
}

menu = ("\t|Menu|\nS - Start\nX - Save\nQ - Quit\nI - Investigate\nZ - inventory\nP - Punch\nB - Batarang\nE - Explosives\nR - Reset")

Start = ('start','s')
Save = ('save','x')
Quit = ('quit','q')
Investigate = ('investigate','i')
Inventory = ('inventory','z')
Punch = ('punch','p')
Batarang = ('batarang','b')
Explosives = ('explosives','e')
Reset = ('reset','r')
choice = ''

