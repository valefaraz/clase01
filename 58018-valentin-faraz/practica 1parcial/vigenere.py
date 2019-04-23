#clave:   LIMELIMELIMELIME                                            
#palabra: WIKIHOWISTHEBEST

def vigenere (palabra,clave):

    abc='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    i=0
    cifrado= ''
    for letter in palabra:
        suma = abc.find(letter) + abc.find(clave[i % len(clave)])
        modulo = int(suma) % len(abc)
        cifrado = cifrado + str(abc[modulo]) 
        i = i+1
    
    return cifrado

    