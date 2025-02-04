import pyxel
#ふたりプレイ用
class Atomic:
    def __init__(self):
        self.x = 0
        self.y = 0
    def update(self):
        self.x = 100
        self.y = 100
    def draw(self):
        pyxel.blt(self.x,self.y,9,120,15,126,0)