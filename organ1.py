from tkinter import *


from random import *
from uuid import *

mapsize = 500
population = 500
sight = 50
speed = 25


##draw base canvas:
master = Tk()
canvas_width = mapsize
canvas_height = mapsize
w = Canvas(master, width=canvas_width, height=canvas_height, bg="Midnight Blue")
w.pack()
x = int(canvas_width / 2)
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")
w.create_line(x, 0, x, canvas_height, fill="#476042")
w.create_line(0, 0, 10, 10, fill="#476042")

    

########objectivy:

class Mover:
    def __init__(self, pos, ME):
        self.pos = pos
        self.ME = ME

    def draw(self):
        w.delete(self.ME)
        w.create_oval(self.pos[0]-2, self.pos[1]-2, self.pos[0]+2, self.pos[1]+2, outline="Dark Sea Green", tag=self.ME)
    
    def move(self):
        
        if self.regard() == "LU":
            self.pos[0] = self.pos[0] - (speed)
            self.pos[1] = self.pos[1] - (speed)

        elif self.regard() == "RU":
            self.pos[0] = self.pos[0] + (speed)
            self.pos[1] = self.pos[1] - (speed)

        elif self.regard() == "LD":
            self.pos[0] = self.pos[0] - (speed)
            self.pos[1] = self.pos[1] + (speed)

        elif self.regard() == "RD":
            self.pos[0] = self.pos[0] + (speed)
            self.pos[1] = self.pos[1] + (speed)

        self.pos[0] = self.pos[0] + randint(-speed, speed)
        self.pos[1] = self.pos[1] + randint(-speed, speed)

        if self.pos[0] > mapsize:
            self.pos[0] -= mapsize
        if self.pos[0] < 0:
            self.pos[0] += mapsize    
        if self.pos[1] > mapsize:
            self.pos[1] -= mapsize
        if self.pos[1] < 0:
            self.pos[1] += mapsize   


        self.draw()

    def regard(self):
        #print("i am " + self.sense + " number " + str(self.ID))
        x_range_low = self.pos[0] - sight
        x_range_high = self.pos[0] + sight
        y_range_low = self.pos[1] - sight
        y_range_high = self.pos[1] + sight

        LUquad = 0
        RUquad = 0
        LDquad = 0
        RDquad = 0
        
        for agent in basket:  
            if agent.pos[0] < x_range_high and agent.pos[0] > x_range_low and agent.pos[1] < y_range_high and agent.pos[1] > y_range_low:
                if agent.pos[0] < self.pos[0] and agent.pos[1] < self.pos[1]:
                    LUquad +=1
                elif agent.pos[0] > self.pos[0] and agent.pos[1] < self.pos[1]:
                    RUquad += 1
                elif agent.pos[0] < self.pos[0] and agent.pos[1] > self.pos[1]:
                    LDquad += 1
                elif agent.pos[0] > self.pos[0] and agent.pos[1] > self.pos[1]:
                    RDquad += 1

        if LUquad > RUquad and LUquad > LDquad and LUquad > RDquad:
            return("LU")
            print("will move LU")
        elif RUquad > LUquad and RUquad > LDquad and RUquad > RDquad:
            return("RU")
            print("will move LU")
        elif LDquad > LUquad and LDquad > RUquad and LDquad > RDquad:
            return("LD")
            print("will move LU")
        elif RDquad > LUquad and RDquad > RUquad and RDquad > LDquad:
            return("RD")
            print("will move LU")
        else:
            return("regarded static")




#populate the pool scene

basket = []
        
def populate():
    global basket
    for i in range(0, population):
        basket.append(Mover([randint(0, mapsize), randint(0, mapsize)], uuid1()))
        basket[i].draw()
    print(len(basket))





#move yixia

def moveyx():
    for mover in basket:
        mover.move()



#finish up canvas and keep it running

Button(master, text="populate", command=populate).pack(side=LEFT)
Button(master, text="move yixia", command=moveyx).pack(side=LEFT)


mainloop()
