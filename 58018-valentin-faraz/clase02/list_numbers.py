def find_max (list_of_numbers):

    if not isinstance(list_of_numbers, list): #True si list_of_numbers  NO es una lista
       raise Exception('not a number')

    if not list_of_numbers:
        return None
    max_number = max (list_of_numbers)
    
    return max_number
