import pyxel


########################
# CONSTANTS FOR WINDOW #
########################

FPS = 30
TITLE = 'RPG'
SIZE_W = 300
SIZE_H = 300
RESOURCES_FILENAME = 'ale.pyxres'


########################
# CONSTANTS FOR IMAGES #
########################

COLOR_KEY = 0 # Color to wrap background.


###########
# CLASSES #
###########

class OnLoadResourses():
    """This class using for loading resources (images, tilemap, music etc.)
    """
    def __init__(self) -> None:
        pyxel.load(RESOURCES_FILENAME)
        
        
class Mag():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.u = 0
        self.v = 0
        self.image = 0
        self.height = 15
        self.width = 15
        self.name = 'Magician'
        self.persona = pyxel.Image(15, 15)
        
        if color == 'yellow':
            self.u = 0
            self.v = 0
        elif color == 'dark':
            self.u = 16
            self.v = 0
        elif color == 'orange':
            self.u = 32
            self.v = 0
        else:
            pass
        
        self.persona = pyxel.blt(self.x, self.y, self.image, self.u, self.v, self.width, self.height, COLOR_KEY)            
    def draw(self, x, y):
        self.persona = pyxel.blt(x, y, self.image, self.u, self.v, self.width, self.height, COLOR_KEY)
        

class App():
    """Class with app definition and initialization.
    """
    def __init__(self) -> None:
        pyxel.init(width=SIZE_W, height=SIZE_H, title=TITLE, fps=FPS)
        OnLoadResourses()
        self.x = 0
        self.mag1 = Mag(0, 0, 'yellow')
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
    def draw(self):
        pyxel.cls(0)
        self.mag1.draw(self.x, 0)
        
        

App()
        