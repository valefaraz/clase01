class Calculadora():
    def __init__(self):
        self.ingresado1=0
        self.ingresado2=0
        self.operador=''
    def ingresar(self,caracter):
        try:
            num1=int(caracter)
            if self.operador==None:
                self.ingresado1 = self.ingresado1*10 + num1
                return
            self.ingresado2=num1

        except:
            operador_anterior=False
            if self.operador != None:
                op_anterior=True
            if caracter== '=':
                if self.operador == '+':
                    self.ingresado1 += self.ingresado2
                if self.operador == '-':
                    self.ingresado1 -= self.ingresado2
                self.operador=''
                self.ingresado2=0
            else:
                self.operador=caracter
                
    
    def display(self):
        return str(self.ingresado1)