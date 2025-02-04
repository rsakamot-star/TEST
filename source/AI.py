import random
import pyxel
import pickle
import requests
#import micropip
#import asyncio
#def install_numpy():
#await micropip.install("numpy")
import numpy as np






class AI_BRAIN:
    def __init__(self):
        self.theta = []
        self.posx = []
        self.posy = []
        self.detx = []
        #self.score = []
        self.y = 0
        self.AfterTrain = False
        self.train_OK = False        
        try:
            self.filename = "/Users/ryunosukesakamoto/work/Game_dir/PYXEL/InvGame/AImodels/model.sav"
            self.model = pickle.load(open(self.filename, 'rb'))
            self.loc = "local"
        except:
            self.LookUpTable = np.load('figures/LookUpTable.npy')
            #print(LookUpTable)
            self.loc = "web"
    def Web(self):
        pass
        if self.train_OK == False:
        #    self.model = pickle.load(open(self.filename, 'rb'))
            #self.model = io.BytesIO(self.response.content)
            #self.model = pickle.load(self.model)
            self.train_OK = True
    def Local(self):
        #if self.train_OK == False:
        #    from sklearn.ensemble import RandomForestRegressor
        #    self.model = RandomForestRegressor()
        pass
    def DeepLearning(self,theta,posx,posy,detx):
        if self.loc == "local":
            self.theta += theta
            self.posx += posx
            self.posy += posy
            self.detx += detx
            #self.score += score
            X = [[self.theta[i],self.posx[i],self.posy[i]] for i in range(len(self.theta))]
            y = self.detx
            self.model.fit(X, y)
            pickle.dump(self.model, open(self.filename, 'ab'))
    def Test(self,theta,x,y,current_x):
        if self.loc == "local":
            X = [[theta,x,y]]
            estx = self.model.predict(X)[0]
            if -25 <= estx <= 200:
                self.y = estx
        if self.loc == "web":
            diff = np.abs(self.LookUpTable[:, 0:3] - np.array([theta, x, y]))
            index_candidates = np.where(np.linalg.norm(diff, axis=1) == np.min(np.linalg.norm(diff, axis=1)))[0]
            final_index = index_candidates[np.argmin(np.abs(self.LookUpTable[index_candidates, 3] - current_x))]
            self.y = np.abs(self.LookUpTable[final_index, 2] - current_x)



class AI_training:
    def __init__(self,app):
        self.app = app
        self.i = 100
        self.theta = []
        self.posx = []
        self.posy = []
        self.detx = []
        self.score = []
        self.objx = []
        self.objy = []
    def update(self):
        self.search()
        if self.app.everyscore > 0:
            self.theta.append(self.app.theta)
            self.posx.append(self.app.x)
            self.posy.append(self.app.y)
            self.detx.append(self.app.cursorX)
            self.score.append(self.app.everyscore)
            self.objx.append(self.app.Fly_bird.objx)
            self.objy.append(self.app.Fly_bird.objy)
    def search(self):
        #self.app.ai_train_move = random.uniform(-30,200)
        if (110 <= self.app.Fly_bird.objy <= 125 and self.app.Fly_bird.objx -30 <= self.app.cursorX <= self.app.Fly_bird.objx):
            if 200 - self.app.cursorX >= 100:
                self.app.cursorX += 3
            if 200 - self.app.cursorX < 100:
                self.app.cursorX -= 33
        elif self.app.ai_train_score_left > self.app.ai_train_score and -25 <= self.app.cursorX <= 200 and self.app.everyscore > 0:
            self.app.cursorX -= 1    #self.app.ai_train_move_left
        elif self.app.ai_train_score_right > self.app.ai_train_score and -25 <= self.app.cursorX <= 200 and self.app.everyscore > 0:
            self.app.cursorX += 1    #self.app.ai_train_move_right
        if self.app.everyscore <= 0:
            self.app.cursorX = random.uniform(-25,200)
            #if (110 <= self.app.Fly_bird.objy <= 125 and self.app.Fly_bird.objx -30 <= self.app.cursorX <= self.app.Fly_bird.objx):
            #    if 200 - self.app.cursorX >= 100:
            #        self.app.cursorX += 3
            #    if 200 - self.app.cursorX < 100:
            #        self.app.cursorX -= 33
            #if self.app.ai_train_move < 200 and self.returns == "DOWN":
            #    self.app.ai_train_move += 1
            #    if self.app.ai_train_move >= 200 : self.returns = "UP"
            #if self.app.ai_train_move >= -30 and self.returns == "UP":
            #    self.app.ai_train_move -= 1
            #    if self.app.ai_train_move <= -30 : self.returns = "DOWN"
        #if self.app.ai_brain.AfterTrain == True:#and self.app.ai_train_score > 0:
        #    self.app.ai_brain.Test([[self.app.theta,self.app.x,self.app.y]])
        #   self.app.cursorX = self.app.ai_brain.y
    def draw(self):
        self.app.cursorX = self.app.cursorX
    def UpdateAIBrain(self):
        self.app.ai_brain.DeepLearning(self.theta,self.posx,self.posy,self.detx)


class cpu:
    def __init__(self,app):
        #self.detector = 
        self.app = app
        self.x = 0
        self.y = 110
        self.score = 0
        self.loc = 0, 24, 32, 16
        self.i = 0
    def update(self):
        if self.app.ai_brain.train_OK == True:
            self.app.ai_brain.Test(self.app.theta,self.app.x,self.app.y,self.app.cursorX)
            self.x = self.app.ai_brain.y
    def draw(self):
        if self.app.ai_brain.train_OK == True:
            if self.i < 7:
                self.i += 0.1
                pyxel.rect(73, 0.01, 43, self.i, 22)
            else:
                pyxel.blt(self.x, 110, 1, self.loc[0], self.loc[1], self.loc[2], self.loc[3], 0)
                pyxel.rect(73, 0.01, 43, 7, 22)
                pyxel.text(75,1,"CPU:",7)
                if self.score > self.app.score:
                    pyxel.text(91,1,str(self.score),23)
                else:
                    pyxel.text(91,1,str(self.score),7)                    


