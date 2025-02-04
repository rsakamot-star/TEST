import pyxel
import requests
import random
import math
import MDT
import AirShower as AS
from flux import Flux
from KeyBoard import GiveName
from timer import *
#from VS import VS
from load_url import *
from Bird import *
import threading
from AI import *

#print(hoge.main())
# T. Abu-Zayyad et.al., The Astrophysical Journal Letters, 768:L1 (5pp), 2013 May 1
# data set: 2008 May 8 and 2012 May

class send_params:
    def __init__(self,zenith,energy,posX,posY,score,app): 
        self.zenith = round(zenith,2)
        self.energy = round(energy,2)
        self.posX = round(posX,2)
        self.posY = round(posY,2)
        self.score = score
        self.app  = app
    def send(self):
        url = "https://rsakamoto.pythonanywhere.com/update_params"
        params = {
                    "zenith": self.zenith, 
                    "energy": self.energy,
                    "posX": self.posX,
                    "posY": self.posY,
                    "score": int(self.score)
                }
        requests.get(url, params=params,timeout=(2,2))
    def estimate(self):
        url = "https://rsakamoto.pythonanywhere.com/estimate_score"
        params = {
                    "zenith": self.zenith, 
                    "energy": self.energy,
                    "posX": self.posX,
                    "posY": self.posY
                }
        res = requests.get(url, params=params).text
        self.app.est_score += float(res[2:-3])

class metal_tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def default_tile_draw(self):
        pyxel.blt(197,0,0,53,8,3,8,0)
        pyxel.blt(197,8,0,53,8,3,8,0)
        pyxel.blt(197,16,0,53,8,3,8,0)
        pyxel.blt(197,24,0,53,8,3,8,0)
        pyxel.blt(197,32,0,53,8,3,8,0)
        pyxel.blt(197,40,0,53,8,3,8,0)
        pyxel.blt(197,48,0,53,8,3,8,0)
        pyxel.blt(197,56,0,53,8,3,8,0)
        pyxel.blt(197,64,0,53,8,3,8,0)
        pyxel.blt(197,72,0,53,8,3,8,0)
        pyxel.blt(197,80,0,53,8,3,8,0)
        pyxel.blt(197,88,0,53,8,3,8,0)

        pyxel.blt(0,0,0,61,8,3,8,0)
        pyxel.blt(0,8,0,61,8,3,8,0)
        pyxel.blt(0,16,0,61,8,3,8,0)
        pyxel.blt(0,24,0,61,8,3,8,0)
        pyxel.blt(0,32,0,61,8,3,8,0)
        pyxel.blt(0,40,0,61,8,3,8,0)
        pyxel.blt(0,48,0,61,8,3,8,0)
        pyxel.blt(0,56,0,61,8,3,8,0)
        pyxel.blt(0,64,0,61,8,3,8,0)
        pyxel.blt(0,72,0,61,8,3,8,0)
        pyxel.blt(0,80,0,61,8,3,8,0)
        pyxel.blt(0,88,0,61,8,3,8,0)
    def hit_tile_draw(self):
        color = 1
        if self.x < 50:
            rl = 61
            pos = 0
        if self.x > 150:
            rl = 53
            pos = 197
        sound_played = False
        if 1 <= self.y <= 7:
            pyxel.blt(pos,0,color,rl,8,3,8,0)
            sound_played = True
        if 9 <= self.y <= 15:
            pyxel.blt(pos,8,color,rl,8,3,8,0)
            sound_played = True
        if 17 <= self.y <= 23:
            pyxel.blt(pos,16,color,rl,8,3,8,0)
            sound_played = True
        if 25 <= self.y <= 31:            
            pyxel.blt(pos,24,color,rl,8,3,8,0)
            sound_played = True
        if 33 <= self.y <= 39:
            pyxel.blt(pos,32,color,rl,8,3,8,0)
            sound_played = True
        if 41 <= self.y <= 47:
            pyxel.blt(pos,40,color,rl,8,3,8,0)
            sound_played = True
        if 49 <= self.y <= 55:
            pyxel.blt(pos,48,color,rl,8,3,8,0)
            sound_played = True
        if 57 <= self.y <= 63:
            pyxel.blt(pos,56,color,rl,8,3,8,0)
            sound_played = True
        if 65 <= self.y <= 71:
            pyxel.blt(pos,64,color,rl,8,3,8,0)
            sound_played = True
        if 73 <= self.y <= 79:
            pyxel.blt(pos,72,color,rl,8,3,8,0)
            sound_played = True
        if 81 <= self.y <= 87:
            pyxel.blt(pos,80,color,rl,8,3,8,0)
            sound_played = True
        if 89 <= self.y <= 95:
            pyxel.blt(pos,88,color,rl,8,3,8,0)
            sound_played = True
        if sound_played:
            pyxel.play(0,3)

class Detector:
    def __init__(self, Option):
        self.opt = Option
    def TASD(self):
        loc = 0, 0, 32, 24
        if self.opt:
            pyxel.blt(33, 40, 1, loc[0], loc[1], loc[2], loc[3], 0)
            pyxel.text(36, 30, "TA SD (1)", 7)
        return loc
    def AugerSD(self):
        loc = 0, 24, 32, 16
        if self.opt:
            pyxel.blt(133, 50, 1, loc[0], loc[1], loc[2], loc[3], 0)
            pyxel.text(126, 30, "Auger SD(2)", 7)
        return loc
    def example1(self):
        loc = 24, 48, 31, 18
        if self.opt:
            pyxel.blt(33, 110, 1, loc[0], loc[1], loc[2], loc[3], 0)
            pyxel.text(36,90,"comming soon\n\n TA FD",7)       
        return loc
    def example2(self):
        loc = 0, 0, 32, 24
        if self.opt:
            #pyxel.blt(33, 40, 1, loc[0], loc[1], loc[2], loc[3], 0)
            pyxel.text(126,90,"comming soon\n\n ?? ??",7)
        return loc
class Menu:
    def __init__(self,app):
        self.state = "main"
        self.detector_type = 1
        self.app = app
        self.Ax = 71
        self.Ay = 78
        #self.opend_url = False
    def update(self):
        if self.state == "main":
            self.app.score = 0
            self.app.x = random.randint(40, 150)
            self.app.y = 0
            self.app.IntDisance = 0
            self.app.r = random.uniform(1,5) 
            self.app.theta = random.randint(30,150)
            self.app.E = Flux(1)
            self.app.run_game = False
            self.app.particle = AS.proton()
            self.app.particles = [None]
            self.app.Get_particles = [None]
            self.app.score = 0
            self.app.geomTheta = [None]
            self.app.geomEnergy = [None]
            self.app.timer = timer()
            self.app.Fly_bird = bird()
            self.app.birdtimerFlag = False
            self.app.timevector = []
            self.app.score_pm = "DEFAULT"
            self.app.IntX = 0
            self.app.Inty = 0
            self.app.INIT = True
            self.app.everyscore = 0
            self.app.ai = "USER"
            self.app.cursorX = 100
            self.app.AI_FLAG = False
            self.app.cpu.score = 0
            self.app.cpu_particles = []
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.app.mode = "VSCPU"
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.app.mode = None
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            ########
            if self.app.mode == "VSCPU":
                self.app.ai_brain.Web()
            if pyxel.btn(pyxel.KEY_A) and pyxel.btn(pyxel.KEY_I):
                self.app.ai = "AI"
                self.state = "start"
                self.app.ai_brain.Local()
                #str(type(self.ai))[7:-2]
            ########
            if pyxel.btnp(pyxel.KEY_SPACE):
                if self.Ay == 78:
                    self.state = "start"
                if self.Ay == 88:
                    self.state = "particles"
                if self.Ay == 98:
                    self.state = "customize"
            if pyxel.btnp(pyxel.KEY_DOWN):
                if self.Ay < 98:
                    self.Ay += 10
            if pyxel.btnp(pyxel.KEY_UP):
                if self.Ay > 78:
                    self.Ay -= 10
            #if pyxel.btnp(pyxel.KEY_S):# or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            #    self.state = "start"
            #if pyxel.btnp(pyxel.KEY_C):
            #    self.state = "customize"
            #if pyxel.btnp(pyxel.KEY_P):
            #    self.state = "particles"
        if self.state == "particles":
            if pyxel.btnp(pyxel.KEY_R):
                self.state = "main"
        if self.state == "customize":
            if pyxel.btnp(pyxel.KEY_1):
                self.detector_type = 1
            if pyxel.btnp(pyxel.KEY_2):
                self.detector_type = 2
            if pyxel.btnp(pyxel.KEY_3):
                self.detector_type = 3
            if pyxel.btnp(pyxel.KEY_4):
                self.detector_type = 4
            if pyxel.btnp(pyxel.KEY_R):
                self.state = "main"
            if pyxel.btnp(pyxel.KEY_LEFT):
                if self.detector_type%2 == 0:
                    self.detector_type -= 1
            if pyxel.btnp(pyxel.KEY_RIGHT):
                if self.detector_type%2 == 1:
                    self.detector_type += 1
            if pyxel.btnp(pyxel.KEY_UP):
                if self.detector_type >= 3:
                    self.detector_type -= 2
            if pyxel.btnp(pyxel.KEY_DOWN):
                if self.detector_type <= 2:
                    self.detector_type += 2
        if self.state == "result":
            self.GiveName = GiveName()
            if pyxel.btn(pyxel.KEY_W):

                self.state = "ranking"
            if pyxel.btnp(pyxel.KEY_R):
                #self.opend_url = False
                self.state = "main"
        if self.state == "ranking":
            self.GiveName.update()
            if pyxel.btnp(pyxel.KEY_RETURN):
                OPENWINDOW = openwindow(self.app.score,self.GiveName.text,self.app.geomTheta,self.app.geomEnergy)
                OPENWINDOW.send_score()
                self.state = "main"
    def draw(self):
        pyxel.cls(0)
        if self.state == "main":
            pyxel.text(80, 30, "COSMIC RAYs", pyxel.frame_count % 16)
            pyxel.text(80, 80, "START GAME", 7)
            pyxel.text(80, 90, "Particles", 7)
            pyxel.text(80, 100, "CUSTOM", 7)

            pyxel.blt(self.Ax, self.Ay, 0, 0,112,7,8, 0)
            pyxel.text(145, 5, "vsCPU:", 20)        
            if self.app.mode == None:
                pyxel.text(170, 5, "ON", 20)
                pyxel.text(180, 5, "OFF", 7)
            if self.app.mode == "VSCPU":
                pyxel.text(170, 5, "ON", 7)
                pyxel.text(180, 5, "OFF", 20)
        if self.state == "particles":
            AS.proton().draw(50,50,18)
            AS.electron().draw(140,50,0)
            AS.gamma().draw(50,114,0)
            AS.muon().draw(140,114,0) 
            pyxel.text(40, 40, "Proton", 7)
            pyxel.text(130, 40, "electron", 7)
            pyxel.text(40, 104, "gamma", 7)
            pyxel.text(130, 104, "muon", 7)         
            pyxel.text(80, 130, "RETURN (r)", 7)
        if self.state == "customize":
            pyxel.text(80, 130, "RETURN (r)", 7)
            Detector(True).TASD()
            Detector(True).AugerSD()
            Detector(True).example1()
            Detector(True).example2()
            if self.detector_type == 1:
                pyxel.rectb(25, 20, 55, 50, pyxel.frame_count % 16)
            if self.detector_type == 2:
                pyxel.rectb(115, 20, 55, 50, pyxel.frame_count % 16)
            if self.detector_type == 3:
                pyxel.rectb(25, 80, 55, 50, pyxel.frame_count % 16) 
            if self.detector_type == 4:
                pyxel.rectb(115, 80, 55, 50, pyxel.frame_count % 16)
        if self.state == "result":
            pyxel.text(25, 60,"Get Particle: " + str(round(self.app.score,1)), 7)
            #pyxel.text(25, 60,"Energy: " + str(self.app.geomEnergy[-1]), 7)
            #pyxel.text(25, 90,"Zenith: " + str(abs(self.app.geomTheta[-1])), 7)
            pyxel.text(25, 130, "Ranking(w)", 7)
            pyxel.text(125, 130, "main menu(r)", 7)
        if self.state == "ranking":
            self.GiveName.draw()
            pyxel.text(75, 40,"Score: " + str(round(self.app.score,1)), 7)
            #pyxel.text(125, 130, "main menu(r)", 7)
            #if not self.opend_url and pyxel.btnp(pyxel.KEY_RETURN):
class Sky:
    def light():
        pyxel.bltm(0, 0, 0, 0, 192, 200, 150)
    def night():
        pyxel.bltm(0, 0, 0, 0, 0, 200, 150)
    def evening():
        pyxel.bltm(0, 0, 0, 0, 384, 200, 150)
    def time():
        #MDT_HH = datetime.datetime.now().hour - 15  # JST -> MDT
        MDT_HH = MDT.get_mdt_time().hour
        #Sky.night()
        #return 7        
        if 0 <= MDT_HH < 4:
            Sky.night()
            return 7
        if 18 <= MDT_HH <= 23:
            Sky.evening()
            return 0
        else:
            Sky.light()
            return 0
class App:
    def __init__(self):
        pyxel.init(200, 150, fps=60,display_scale=5)   
        pyxel.screen_mode(0)   
        pyxel.cls(0)
        self.detx = 100
        self.x = random.randint(40, 150)
        self.y = 0
        self.IntDisance = 0
        self.r = random.uniform(1,5) 
        self.theta = random.uniform(30,150)
        self.menu = Menu(self)
        self.E = Flux(1)
        self.run_game = False
        self.particle = AS.proton()
        self.particles = [None] 
        self.score = 0
        self.geomTheta = [None]
        self.geomEnergy = [None]
        self.Fly_bird = bird()
        self.score_pm = "DEFAULT"
        self.birdtimerFlag = False
        self.IntX = 0
        self.IntY = 0
        self.timevector = []
        self.INIT = True
        self.everyscore = 0
        self.est_score = 0
        self.metal_tiles = metal_tile(100,0)
        self.ai = "USER"
        self.cursorX = 100
        self.AI_FLAG = False
        self.ai_brain = AI_BRAIN()
        self.ai_train_score,self.ai_train_score_left,self.ai_train_score_right = 0,0,0
        self.loc = Detector(False).TASD()
        self.mode = None
        self.cpu = cpu(self)
        self.cpu_particles = []
        #self.atom = Atomic()
        pyxel.mouse(False)
        pyxel.load('figures/star.pyxres')
        pyxel.run(self.update, self.draw)
    def update(self):
        self.menu.update()
        if self.menu.state == "start":
            self.run_game = True
        else:
            self.run_game = False
        if self.run_game:
            if self.mode == "VSCPU":
                self.cpu.update()
            #if self.ai == "AI":
            #    self.train_ai = AI_training(self)
            self.timer.update()
            self.Fly_bird.update()
            if self.timer.Init >= 30 and self.ai == "USER":
                self.menu.state = "result"
            if self.IntDisance >= self.r * math.sin(self.theta*math.pi/180):
                self.IntDisance = 0
                self.r = 1
                if 15 <= self.y <= 120:
                    #for _ in range(random.randint(50,100)):
                    if  self.IntY == 0 and self.IntX == 0:
                        self.IntX = self.x
                        self.IntY = self.y
                    k = random.randint(50,100)
                    self.particle = random.choices([AS.muon(),AS.gamma(),AS.electron()],k=k,weights=[2,1,2])
                    for part in self.particle:
                        self.particles.append(AS.airshowers(self.x,self.y,part,self.theta,self.E))
            if self.y < 300:
                self.x += math.cos(self.theta*math.pi/180)
                self.y += math.sin(self.theta*math.pi/180)
                self.IntDisance += math.sin(self.theta*math.pi/180)
            if self.y >= 300 or 0 < len(self.particles) <= 5 or self.x < -1000 or self.x > 1000:
                if self.INIT != True and self.everyscore > 0:
                    pass
                    #self.params=send_params(self.theta-90,self.E,self.x,self.y,self.everyscore,self)
                    #self.thread = threading.Thread(target=self.params.send)
                self.INIT = False
                self.geomTheta.append(abs(self.theta-90))
                self.geomEnergy.append(self.E)
                self.everyscore = 0
                self.y = 0
                self.E = Flux(1)
                self.theta = random.uniform(30,150)
                self.r = random.uniform(1,5) 
                self.x = random.randint(40, 150)
                self.particle = AS.proton()
                self.particles,self.cpu_particles = [],[]
                self.IntX = 0
                self.Inty = 0
                if self.ai == "AI":
                    if self.AI_FLAG == True:
                        self.train_ai.UpdateAIBrain()
                        self.AI_FLAG = False
                    self.train_ai = AI_training(self)
                    self.AI_FLAG = True
            if not isinstance(self.particle, AS.proton):
                for p in self.particles:
                    p.update()
            self.particles = [p for p in self.particles if p.y <= 140 and 0 < p.x < 200]
            Lost_particles = []
            self.metal_tile_range = []
            self.ai_train_score,self.ai_train_score_left,self.ai_train_score_right = 0,0,0
            for p in self.particles:
                if 120 <= p.y <= 125 and p.x - 30 <= self.cursorX <= p.x and not isinstance(p.p, AS.gamma):
                    if self.score_pm == "DEFAULT":
                        self.score += 1
                        self.everyscore += 1
                    if self.score_pm == "DAMEGE" and random.random() < 0.5:
                        self.score += 1
                        self.everyscore += 1
                    if self.score_pm == "STAR":
                        self.score += 1
                        self.everyscore += 1
                    pyxel.play(0,2)
                else:
                    if 3 > p.x:
                        self.metal_tile_range.append(metal_tile(p.x,p.y))
                        p.deg = abs(180 - p.deg)
                        p.r += 1
                    if p.x > 197:
                        self.metal_tile_range.append(metal_tile(p.x,p.y))
                        p.deg = abs(180 - p.deg)
                        p.r += 1
                    Lost_particles.append(p)
                if self.ai == "AI":
                    if 120 <= p.y <= 125 and p.x - 30 <= self.cursorX <= p.x and not isinstance(p.p, AS.gamma):
                        self.ai_train_score += 1
                    if 120 <= p.y <= 125 and p.x - 30 <= self.cursorX -1 <= p.x and not isinstance(p.p, AS.gamma):
                        self.ai_train_score_left += 1
                    if 120 <= p.y <= 125 and p.x - 30 <= self.cursorX +1 <= p.x and not isinstance(p.p, AS.gamma):
                        self.ai_train_score_right += 1
                if 120 <= p.y <= 125 and p.x - 30 <= self.cpu.x <= p.x and not isinstance(p.p, AS.gamma) and self.mode == "VSCPU":
                    if not p in self.cpu_particles:
                        self.cpu_particles.append(p)
                        self.cpu.score += 1
            self.particles = Lost_particles
            #if 3 > self.x:
            #    self.theta = abs(180 - p.deg)
            #if self.x > 197:
            #    self.theta = abs(180 - p.deg)
            if pyxel.btnp(pyxel.KEY_F):
                self.menu.state = "result"
                self.run_game = False
            if self.Fly_bird.objx -30 <= self.cursorX <= self.Fly_bird.objx and  116 <= self.Fly_bird.objy <= 120:
                self.birdtimer = conter(100)
                self.birdtimerFlag = True
                self.Fly_bird.Flag = True
                self.Fly_bird.objy = -1
                if self.Fly_bird.char == "STAR":
                    self.timer.Count_pm(-3)
                    self.score_pm = "STAR"
                if self.Fly_bird.char == "HUN":
                    self.timer.Count_pm(3)
                    self.score_pm = "DAMEGE"
            if self.ai == "AI":
                self.train_ai.update()
    def draw(self):
        FontColor = Sky.time()
        self.timer.draw(FontColor)
        if self.menu.state == "main" or self.menu.state == "customize" or self.menu.state == "particles" or self.menu.state == "result" or self.menu.state == "ranking":
            self.menu.draw()
        if self.run_game:
            #self.atom.draw()
            self.metal_tiles.default_tile_draw()
            for j in self.metal_tile_range:
                j.hit_tile_draw()
            if self.menu.detector_type == 1:
                self.loc = Detector(False).TASD()
            if self.menu.detector_type == 2:
                self.loc = Detector(False).AugerSD()
            if self.menu.detector_type == 3:
                self.loc = Detector(False).example1()
            if self.menu.detector_type == 4:
                self.loc = Detector(False).example2()
            if self.mode == "VSCPU":
                if self.menu.detector_type != 2:
                    self.cpu.loc = Detector(False).AugerSD()
                else:
                    self.cpu.loc = Detector(False).TASD()
                self.cpu.draw()
            if self.ai == "AI":
                self.train_ai.draw()
            if self.ai == "USER":
                self.cursorX = pyxel.mouse_x
            pyxel.blt(self.cursorX, 110, 1, self.loc[0], self.loc[1], self.loc[2], self.loc[3], 0)
            pyxel.rect(0, 140, 200, 10, 0)
            pyxel.text(160, 142, "result(f)", 11)
            pyxel.text(60,142,"MDT:"+str(MDT.get_mdt_time().strftime('%Y-%m-%d %H:%M:%S')),7)
            if not isinstance(self.particle, AS.proton):
                for p in self.particles:
                    p.draw()
            else:
                self.particle.draw(self.x,self.y,self.E)
            pyxel.text(0,142,str(self.score),7)
            self.Fly_bird.draw()
            if self.birdtimerFlag == True and self.Fly_bird.Flag == True:
                if self.Fly_bird.char == "STAR" and self.Fly_bird.objy == -1:  
                    self.timevector.append(timeCountText(FontColor," - 3.0"))
                if self.Fly_bird.char == "HUN" and self.Fly_bird.objy == -1:   
                    self.timevector.append(timeCountText(FontColor," + 3.0"))
                self.timevector[-1].draw()
                if self.birdtimer.corr() == "FINISH":
                    self.birdtimerFlag = False
                    self.score_pm = "DEFAULT"
                    self.timevector.pop(0)
            #pyxel.text(30,100,str(int(self.est_score)),0)
App()