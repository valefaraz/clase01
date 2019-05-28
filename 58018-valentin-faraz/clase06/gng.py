class Game():
    def __init__(self):
        self.is_playing = True
    def finish(self):
        self.is_playing = False

class HumanAgainstComputerGame(Game):

    def __init__(self):
        #self.is_playing = True (se borra porque creamos una clase en comun)
        super __init__() #hereda el init de la clase base
        self.secret_number = rand int ()
    
    def play(self,number):
        if self.secret_number > number:
            return "My number is bigger"
        if self.secret_number < number:
            return "My number is smaller"
        self.is_playing = False
            return "You win"
class ComputerAgainstHumanGame(Game):

    def __init__(self):
        #self.is_playing = True (se borra porque creamos una clase en comun)
        super __init__()
        self.cota_max = 100
        self.cota_min = 0
    def input_text(self):
    
    def play(self,respuesta):
        self.cota_max