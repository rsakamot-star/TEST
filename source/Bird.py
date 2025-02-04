import pyxel
import random


class Hun:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def update(self):
        self.y += 1.5
    def star(self):
        #pyxel.circ(self.x, self.y, 2, pyxel.frame_count % 20)
        pyxel.blt(self.x, self.y, 0, 16, 104, 8, 8, 0)
    def hun(self):
        pyxel.blt(self.x, self.y, 0, 65, 120, 6, 16, 0)


class bird:
    def __init__(self):
        self.x = 200
        self.y = random.uniform(5,20)
        self.Image = -32
        self.Flag = True
        self.objx = -100
        self.objy = -100
    def update(self):
        if random.random() < 0.1 and self.Flag == True:
            self.hun = Hun(self.x,self.y+8)
            self.Flag = False
            self.char = random.choices(["HUN","STAR"],k=1,weights=[9,1])[0]
        if self.Flag == False:
            self.hun.update()
            if self.hun.y >= 150 or self.objy == -1:
                self.objy = -100
                self.Flag = True
        if -20 < self.x:
            self.x -= 1
        if -20 >= self.x:
            self.x = 200
            self.y = random.uniform(5,20)
        if self.Image != 160:
            self.Image += 16
        if self.Image == 160:
            self.Image = -160
    def draw(self):
        pyxel.blt(self.x, self.y, 0, abs(self.Image), 136, 17, 16, 0)
        if self.Flag == False:
            if self.char == "STAR":self.hun.star()
            if self.char == "HUN":self.hun.hun()
            self.objx = self.hun.x
            self.objy = self.hun.y


