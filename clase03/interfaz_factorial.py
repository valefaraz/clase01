
class Notnumberexeption(Exception)
    pass

def main():
    palabra=input('Ingrese un numero')
    result=interfaz_factorial(palabra)
    print(result)

def interfaz_factorial (palabra):
   from factorial import factorial
   try:
    n=int(palabra)
    return factorial(n)

   except:
    return 'Error'   
    
    
    if not isinstance (number,int):
        return 'Error'
