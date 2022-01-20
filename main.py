import pyxel


class App():
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        pyxel.init(100, 100, fps=60)
        pyxel.load('ale.pyxres')
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.x += 1
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 15, 15, 0)
        
App()
        