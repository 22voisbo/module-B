# File: convert.py
# A program to convert Celsius temps to Fahrenheit
# Modified 05/01/19
# By:Bonnie Voisine

def ctf():
    for i in range(5):
        Celsius = eval(input("What is the Celsius temperature? "))
        Fahrenheit = 9 / 5 * Celsius + 32
        print("The temperature is", Fahrenheit, "degrees Fahrenheit.")
        print(" ")
    


def ftc():
    for i in range(5):
        Fahrenheit = eval(input("What is the fahrenheit temperature?"))
        Celsius = (Fahrenheit-32)*5/9 
        print("The temperature is",Celsius,"degrees celsius.")
        print(" ")

def main():
    print("Convert Celsius to Fahrenheit")
    print("Celsius temperature \t Fahrenheit Equivalent")
    for currentCelsiusTemperature in range(0,101,10):
        fahrenheitTemperatureEquvalent = ( 9 / 5 ) *currentCelsiusTemperature + 32
        print( currentCelsiusTemperature,"°C","\t\t\t",fahrenheitTemperatureEquvalent,"°F")
    uc = input("Do you want to convert C-->F(c) or F-->C(f) or quit(q):")
    while uc !='q':
        if uc == 'c':
            ctf()
            uc = input("Do you want to convert C-->(c) ro F-->(f) or quit(q): ")
        elif uc == 'f':
            ftc()
            uc = input("Do you want to convert C--F(c) or F-->(f) or quit(q): ")
        elif uc !='c' and uc !='f':
            print("Please put a VALID INPUT!")
            uc = input("Do you want to convert C-->F(c) or F-->C(f) or quit(q): ")
    print("Now exiting...")

main()