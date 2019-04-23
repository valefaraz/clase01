from vigenere import vigenere


def main():
    mensaje = input("Ingrese el mensaje a codificar: ")
    clave = input("Ingrese la clave: ")
    resultado = interfaz(mensaje,clave)
    print(resultado)


def interfaz(mensaje,clave):
    resultado = vigenere(mensaje,clave)
    return resultado




