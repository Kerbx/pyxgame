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

class DialogSystem():
    """This class simulating dialog system.
    """
    def __init__(self, file) -> None:
        self.dialog_file = file
        pyxel.bltm(DIALOG_POS_X, DIALOG_POS_Y, DIALOG_TILEMAP, DIALOG_U, DIALOG_V, DIALOG_WIDTH, DIALOG_HEIGHT, DIALOG_COLOR_KEY)
    
    def narrative(self) -> None:
        with open(self.dialog_file) as dialog_file:
            dialog_answers = list(filter(lambda string: string.startswith(ANSWER_SYMBOL), list(dialog_file)))
            for row in dialog_file:
                print(row)
                if pyxel.btn(pyxel.KEY_E):
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
        
        
class Mag():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.u = 0
        self.v = 0
        self.image = 0
        self.height = 16
        self.width = 16
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
        self.mag1 = Mag(0, 0, 'yellow')
        self.dia = DialogSystem('dialogSystem/magician.txt')
        pyxel.run(self.update, self.draw)
    def update(self):
        self.dia.narrative()
    def draw(self):
        pyxel.cls(0)
        self.mag1.draw(self.x, 0)
    

App()
        