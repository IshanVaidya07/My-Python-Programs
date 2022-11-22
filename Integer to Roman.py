import colorama # For Coloring the text
from colorama import Fore # Fore command is used for font coloring

def int_to_roman(x):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX','X','XL','L','XC','CD','D','LM','M']
    i = 12 # As in the number's list the 12th element is 1000
    roman_numeral = '' # Empty string
    while x != 0:
        if numbers[i] <= x:
            roman_numeral = roman_numeral + roman[i] # Adding the value of roman[i] to the empty string roman_numeral
            x = x-numbers[i]
        else:
            i = i-1
    return roman_numeral

inp_num = int(input("Enter the number of which Roman Symbolic Representation is needed : "))
conversion = int_to_roman(inp_num)
print("The roman representation of the number ", inp_num , "is", Fore.GREEN  + "\033[1m" + conversion + "\033[0m") # \033[1m" + conversion + "\033[0m -- for bolding the text