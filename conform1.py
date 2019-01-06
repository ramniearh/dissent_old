# set up libraries and system
import random 

mapsize = 500
population = 1000
sight = 50
speed = 50
sense_basket = ["#8a2be2", "#556b2f"]

import time
print(time)
print(random.random())

#set up tk graphics
from tkinter import *
master = Tk()

canvas_width = mapsize
canvas_height = mapsize
w = Canvas(master, width=canvas_width, height=canvas_height, bg="#0A0628")
w.pack()

x = int(canvas_width / 2)
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
w.create_line(x, 0, x, canvas_height)
w.create_line(0, 0, 10, 10, fill="#778899")



###begin objectification
class Agent:
    def __init__(self, pos, sense, ID, plok):
        self.pos = pos
        self.sense = sense
        self.ID = ID
        self.draw()
        self.plok = plok
        #self.age = age

    def draw(self):
        
        w.create_oval(self.pos[0]-3, self.pos[1]-3, self.pos[0]+3, self.pos[1]+3, fill=self.sense)

    def move(self):
        #print(self.pos)
        self.pos[0] = self.pos[0] + (speed * random.randint(-2, 2))
        if self.pos[0] > mapsize:
            self.pos[0] -= mapsize
        if self.pos[0] < 0:
            self.pos[0] += mapsize    
        self.pos[1] = self.pos[1] + (speed * random.randint(-2, 2))
        if self.pos[1] > mapsize:
            self.pos[1] -= mapsize
        if self.pos[1] < 0:
            self.pos[1] += mapsize   
        self.draw()

    def change(self):
        if random.random() < self.plok:
            if self.sense == "#8a2be2":
                self.sense = "#556b2f"
            else:
                self.sense = "#8a2be2"
        
    def regard(self):
        #print("i am " + self.sense + " number " + str(self.ID))
        x_range_low = self.pos[0] - sight
        x_range_high = self.pos[0] + sight
        y_range_low = self.pos[1] - sight
        y_range_high = self.pos[1] + sight

        neighbors_same = 0
        neighbors_dif = 0
        
        for agent in basket:  
            if agent.pos[0] < x_range_high and agent.pos[0] > x_range_low and agent.pos[1] < y_range_high and agent.pos[1] > y_range_low:
                
                if agent.sense == self.sense:
                    neighbors_same += 1
                    
                else:
                    neighbors_dif += 1
                    
        if neighbors_dif > neighbors_same:
            self.change()
        #else:
         #   self.move()
        self.draw()

       
            
### end objetification


#populate the circus scene

basket = []
        
def populate():
    global basket
    for i in range(0, population):
        basket.append(Agent([random.randint(0, mapsize), random.randint(0, mapsize)], random.choice(sense_basket), i, random.random()))
    print(len(basket))

#populate()


#kan yixia

def kan_yx():
    w.delete(ALL)
    print("kan")
    print(len(basket))
    for agent in basket:
        agent.regard()
    print(len(basket))

#kan_yx()

def move_about():
    w.delete(ALL)
    for agent in basket:
        agent.move()


#automate

def flow():
    move_about()
    kan_yx()
    #time it

#reset

def reset():
    global basket
    w.delete(ALL)
    basket = []
    print(len(basket))


#print debug
def printit():
    print(basket[5])
    print(basket[population - 10])
    

#run tk graphics
pop_butt = Button(master, text="populate", command=populate)
pop_butt.pack(side=RIGHT)

kan_butt = Button(master, text="kan yixia", command=kan_yx)
kan_butt.pack(side=LEFT)

move_butt = Button(master, text="move about", command=move_about)
move_butt.pack(side=LEFT)

flow_butt = Button(master, text="flow", command=flow)
flow_butt.pack(side=LEFT)

reset_butt = Button(master, text="reset", command=reset)
reset_butt.pack(side=RIGHT)


Button(master, text="printit", command=printit).pack()

mainloop()
