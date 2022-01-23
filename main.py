import pyxel


#############################
# CONSTANTS FOR APPLICATION #
#############################

FPS = 30
TITLE = 'RPG'
SIZE_W = 300
SIZE_H = 300
RESOURCES_FILENAME = 'ale.pyxres'


########################
# CONSTANTS FOR IMAGES #
########################

COLOR_KEY = 0 # Color to wrap background.
DIALOG_WIDTH = 256
DIALOG_HEIGHT = 64


###############################
# CONSTANTS FOR DIALOG SYSTEM #
###############################

DIALOG_TILEMAP = 0
DIALOG_U = 0
DIALOG_V = 0
DIALOG_POS_X = 0
DIALOG_POS_Y = 236
DIALOG_COLOR_KEY = 0
DIALOG_COLOR = 4
NARRATIVE_SYMBOL = '#'
QUESTION_SYMBOL = '?'
ANSWER_SYMBOL = '&'


###########
# CLASSES #
###########

class Person():
    """Parent class for all persons in game.
    """
    name = ''
    x = 0
    y = 0
    image = 0
    u = 0
    v = 0
    width = 16
    height = 16


class MainCharacter(Person):
    """Class for main character.
    """
    def __init__(self, name) -> None:
        self.name = name
        self.u = 0
        self.v = 16
        self.hero = pyxel.Image(self.width, self.height)
        self.hero = pyxel.blt(self.x, self.y, self.image, self.u, self. v, self.width, self.height, COLOR_KEY)

    def walking(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1
        elif pyxel.btn(pyxel.KEY_S):
            self.y += 1
        elif pyxel.btn(pyxel.KEY_D):
            self.x += 1
        elif pyxel.btn(pyxel.KEY_A):
            self.x -= 1
    
    def draw(self):
        self.hero = pyxel.blt(self.x, self.y, self.image, self.u, self.v, self.width, self.height, COLOR_KEY)
        
    def toSpeak(self) -> None:
        self.dialog = DialogSystem('dialogSystem/magician.txt')
        self.dialog.show()
        self.dialog.narrative()
 
        
class DialogSystem():
    """This class simulating dialog system.
    """
    def __init__(self, file) -> None:
        self.dialog_file = file
    
    def show(self) -> None:
        pyxel.bltm(DIALOG_POS_X, DIALOG_POS_Y, DIALOG_TILEMAP, DIALOG_U, DIALOG_V, DIALOG_WIDTH, DIALOG_HEIGHT, DIALOG_COLOR_KEY)
            
    def narrative(self) -> None:
        dialog_answers = ''
        with open(self.dialog_file) as dialog_file:
            dialog_answers = list(filter(lambda string: string.startswith(ANSWER_SYMBOL), list(dialog_file)))
        
        with open(self.dialog_file) as dialog_file:
            for row in dialog_file:
                if pyxel.btn(pyxel.KEY_B):
                    if row.startswith(NARRATIVE_SYMBOL):
                        pyxel.text(6, 240, row[1:], DIALOG_COLOR)
                    elif row.startswith(QUESTION_SYMBOL):
                        pyxel.text(6, 240, row[1:], DIALOG_COLOR)
                        for answers in dialog_answers:
                            a = answers
                            answers = answers[1:-1]
                            answers = answers.split(sep='|')
                            i = 1
                            for answer in answers:
                                pyxel.text(6, 240 + 6 * i, str(i) + ' ' + answer, DIALOG_COLOR)
                            dialog_answers.remove(a)   
                
                
class OnLoadResourses():
    """This class using for loading resources (images, tilemap, music etc.)
    """
    def __init__(self) -> None:
        pyxel.load(RESOURCES_FILENAME)
        
        
class Mag(Person):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.name = 'Magician'
        self.persona = pyxel.Image(self.width, self.height)
        
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
        self.hero = MainCharacter('Lukich')
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.hero.walking()
    def draw(self):
        pyxel.cls(0)
        self.hero.draw()
        if pyxel.btn(pyxel.KEY_E):
            self.hero.toSpeak()
            
    
App()
        