import pyxel
class GiveName:
    def __init__(self):
        pyxel.cls(0)
        self.text = ""
    def update(self):
        for key in range(256):
            if pyxel.btnp(key):
                if key == pyxel.KEY_BACKSPACE and 0 < len(self.text):
                    self.text = self.text[:-1]
                if key == pyxel.KEY_SPACE and len(self.text)<=10:
                    self.text += " "
                if len(self.text)<=10:
                    if 32 <= key <= 126:
                        self.text += chr(key)
    def draw(self):
        pyxel.cls(0)
        pyxel.text(100-len(self.text)*2,70,self.text,7)
        if len(self.text)<=10:
            if pyxel.frame_count%16 < 8:
                pyxel.rect(100+len(self.text)*2,75,3,1,0)
            else:
                pyxel.rect(100+len(self.text)*2,75,3,1,7)
        pyxel.text(125, 80, "<- ENTER ->", 7)