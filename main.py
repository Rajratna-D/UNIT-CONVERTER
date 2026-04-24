#This Program hepls you convert different units
#ther are 3 units here Length,Time,TEmperatue

#code b;ock for lenght
def length_converter():
    print("""1: Meter to Centimeter
2: Centimeter to Meter""")
    
    choice = int(input("Enter your choice: "))
    
    value = float(input("Enter your value: "))
    
    if choice == 1:
        print("Meter to Centimeter =", round(value * 100, 4), "cm")
    elif choice == 2:
        print("Centimeter to Meter =", round(value / 100, 4), "m")
    else:
        print("Invalid choice!")

#code block for time
def time_converter():
    print("""1: Seconds to Minutes
2: Minutes to Hours
3: Hours to Days
4: Days to Years""")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter your value: "))

    if choice == 1:
        print("Seconds to Minutes =", round(value / 60, 4), "min")
    elif choice == 2:
        print("Minutes to Hours =", round(value / 60, 4), "hours")
    elif choice == 3:
        print("Hours to Days =", round(value / 24, 4), "days")
    elif choice == 4:
        print("Days to Years =", round(value / 365, 4), "years")
    else:
        print("Invalid choice!")

#code block for temperature
def temperature_converter():
    print("""1: Celsius to Fahrenheit
2: Fahrenheit to Celsius
3: Celsius to Kelvin
4: Kelvin to Celsius""")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter your value: "))

    if choice == 1:
        print("Celsius to Fahrenheit =", round((value * 9/5) + 32, 4), "F")
    elif choice == 2:
        print("Fahrenheit to Celsius =", round((value - 32) * 5/9, 4), "C")
    elif choice == 3:
        print("Celsius to Kelvin =", round(value + 273.15, 4), "K")
    elif choice == 4:
        print("Kelvin to Celsius =", round(value - 273.15, 4), "C")
    else:
        print("Invalid choice!")

#this while loop here helps us to keep on running the program 
#so that the user can keep on getting different outputs according to it's needs
while True:
    print("UNIT CONVERTER ")
    print("1: Length")
    print("2: Time")
    print("3: Temperature")
    print("0: Exit")

    a = int(input("Enter your choice: "))

    if a == 1:
        length_converter()
    elif a == 2:
        time_converter()
    elif a == 3:
        temperature_converter()
    elif a == 0:
        print("Thankyou for using !")
        break
    else:
        print("Invalid choice!")
