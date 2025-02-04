import pyxel

class conter:
    def __init__(self,second):
        self.init = pyxel.frame_count + second # please input second
        #self.second = second * 600
    #def cont(self):
    #        self.init += 1/60
    def corr(self):
        if pyxel.frame_count > self.init:
            return "FINISH"
        else:
            pass

class timer:
    def __init__(self):
        self.Init = 0
        self.Flag = True
    def update(self):
        self.Init += 1/60     
        self.Flag = True
    def draw(self,FontColor):
        pyxel.text(5,5,str(round(self.Init,1)),FontColor)
    def Count_pm(self,score):
        if self.Flag == True:
            self.Init += score
            self.Flag = False
class timeCountText:
    def __init__(self,FontColor,strtime):
        self.time = strtime
        self.FontColor = FontColor
    def draw(self):
        pyxel.text(20,5,self.time,self.FontColor)
        