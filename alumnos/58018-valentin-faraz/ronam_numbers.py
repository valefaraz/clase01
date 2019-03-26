def roman_to_decimal(roman_number):
    #if roman_number =='I':
    #    return 1
    #else:
    #    return 2
    #reemplazamos el if por un for para que realice los calculos
    decimal_number=0
    ant=''
    for letter in roman_number:
        if letter == 'I':
            decimal_number +=1
        if letter == 'V':
            decimal_number +=5
            if ant=='I':
                decimal_number -=2
        if letter == 'X':
            decimal_number +=10
            if ant=='I':
                decimal_number -=2
        if letter == 'L':
            decimal_number +=50
            if ant == 'X':
                decimal_number -=20
        if letter == 'C':
            decimal_number +=100
        ant=letter    
    return decimal_number
    

    
