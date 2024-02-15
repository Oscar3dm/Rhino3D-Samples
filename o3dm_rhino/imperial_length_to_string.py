from fractions import Fraction
#Component Inputs: length_decimal, round_factor

def imperial_length_to_string(length_decimal, round_factor):
    if round_factor:
        length_decimal = round(length_decimal / round_factor) * round_factor

    #Seperate the length into feet and inches
    feet = int(length_decimal // 12)
    inches = length_decimal % 12
    #Get the decimal and whole number portions of inches
    inches_decimal = inches%1
    inches_whole = int(inches)
    #Calculate the fraction string if we have a decimal
    fraction = ""
    if inches_decimal:
        fraction = Fraction(inches_decimal).limit_denominator()
    #Concatenate the length strings
    length = ""
    if feet:
        length+=str(feet)+"'"
    if feet and inches:
        length+="-"
    if inches_whole:
        length+=str(inches_whole)
    if inches_whole and inches_decimal:
        length+=" "
    if inches_decimal:
        length+=str(fraction)
    #Set length to 0 if it's still empty
    if not length:
        length = "0"
    if inches:
        length+="\""
    return length