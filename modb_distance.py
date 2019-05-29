def main():
    kilometers = float(input("Enter a distance in kilometers: "))
    conv_fac = 1.609 #conversion factor 
    #calculating how many miles 
    miles = round(kilometers / conv_fac,5)
    print("The distance in miles is: ", miles)
main()