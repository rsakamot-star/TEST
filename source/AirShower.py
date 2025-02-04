import pyxel
import random
import math

class muon:
    def draw(self,x,y,E):
        pyxel.circ(x, y,0.3,16) 
        #pyxel.blt(x,y,0,3,120,3,3,0)
class electron:
    def draw(self,x,y,E):
        pyxel.circ(x, y,0.3,18)
        #pyxel.blt(x,y,0,0,123,3,3,0)
class gamma:
    def draw(self,x,y,E):
        pyxel.circ(x, y,0.3, 17) 
        #pyxel.blt(x,y,0,0,120,3,3,0)
class proton:
    def draw(self,x,y,E):
        pyxel.circ(x, y, 21 - E, 19)

#class particles:
#    def __init__(self):
#        self.x = x


class airshowers:
    def __init__(self,x,y,p,theta,E):
        self.x = x 
        self.y = y    
        self.p = p
        self.E = E
        self.theta = theta
        self.r = random.uniform(0.1,2.5)
        self.deg = random.uniform(-self.E,self.E) + self.theta 
        self.dtheta = 0
    def update(self):
        self.x += math.cos((self.deg+self.dtheta)*math.pi/180) * self.r
        self.y += math.sin((self.deg+self.dtheta)*math.pi/180) * self.r
        if self.r < 1:
            self.r += 0.002
        self.dtheta = random.uniform(-self.E*3,self.E*3)
    def draw(self):
        self.p.draw(self.x,self.y,0)


