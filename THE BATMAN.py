def get_input(question, answers):
    player = ""
    while player not in  answers:
        print(question)
        for x in answers:
            print(x)
        player =input()
    return player

class Inventory:
    def __init__(self,D):
        self.D = D  

    def storage(self):
        for D in self.D:
            print(D + " " + str(self.D[D]))
        
    def add(self,item):
        if item in self.D:
            self.D[item] += 1
        else:
            self.D[item] = 1
    
    def remove(self,item):
        if item in self.D:
            self.D[item] -= 1
            if self.D[item] == 0:
                self.D.pop(item)
             

inv = {
    "paper": 1,
    "pencil": 3,
    "eraser": 1
}

Steve = Inventory(inv)

Steve.storage()