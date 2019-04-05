def decimal_to_roman(decimal):
    
    unidad = ''
    roman_number = ''
    decimal_string = str(decimal)

    if decimal_string[0] == '1':
        unidad = 'I'
    if decimal_string[0] == '2':
        unidad = 'II'
    if decimal_string[0] == '3':
        unidad = 'III'
    if decimal_string[0] == '4':
        unidad = 'IV'
    if decimal_string[0] == '5':
        unidad = 'V'
    if decimal_string[0] == '6':
        unidad = 'VI'
    if decimal_string[0] == '7':
        unidad = 'VII'
    if decimal_string[0] == '8':
        unidad = 'VIII'
    if decimal_string[0] == '9':
        unidad = 'IX'
    else:
        roman_number = unidad
    return (roman_number)