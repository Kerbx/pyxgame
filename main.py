import pyxel


#############
# CONSTANTS #
#############

FPS = 30
TITLE = 'RPG'
SIZE_W = 300
SIZE_H = 300
RESOURCES_FILENAME = 'ale.pyxres'


###########
# CLASSES #
###########

class OnLoadResourses():
    """This class using for loading resources (images, tilemap, music etc.)
    """
    def __init__(self) -> None:
        pyxel.load(RESOURCES_FILENAME)
        
        
class Mag():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.name = 'Magician'


class App():
    """Class with app definition and initialization.
    """
    def __init__(self) -> None:
        pyxel.init(width=SIZE_W, height=SIZE_H, title=TITLE, fps=FPS)
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        
App()
        