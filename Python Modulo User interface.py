# Modulo in python


print("Welcome to Judith Modulo Userinterface.")


print("Enter a number of seconds to find the minute and seconds")
print("This output number of Munites and Seconds using user input")
try: 

    number_seconds = int(input("Enter a number of seconds: "))
    if number_seconds < 60:
        raise ValueError("interger must be above 60")
    

    minutes = number_seconds// 60
    seconds = number_seconds % 60
    print(f"{number_seconds} seconds is {minutes}minutes and {seconds}seconds. ")

except ValueError as error:
    print("Error: ", str(error))



print("ENTER TWO HOUR BETWEEN 1 AND 12: The first is the current hour, the second is the hour aheads")
print("This will output future_hour")
try:

    hour1 = int(input("Enter an hour : "))
    hour2 = int(input("How many hours aheads: "))

    if hour1 < 1 or hour2 < 1:
        raise ValueError("Hour must between 1 and 12")
    

    future_hour = (hour1 + hour2) % 12
    print(f"The future hour is: ", future_hour)

except ValueError as error:
    print("Error: ", str(error))




print("Find the last Digit of 2 raised to the power of number/user_input.")

try:
    user_input = int(input("Enter a power: "))

    if user_input < 0:
        raise ValueError("power must be positive interger.")
    

    power = user_input**2 % 10
    print("The last digit of power raised to 2 is: ", power)

except ValueError as error:
    print("Error: ", str(error))





print("Find the last two Digit of 2 raised to the power of number/ user_input.")

try: 

    user_input = int(input("Enter a power: "))

    if user_input < 0:
       raise ValueError("Power must be a positive interger")
    
    power = user_input**2 % 100
    print("The last two digit are: ",power)

except ValueError as error:
    print("Error: ", str(error))




print("Enter a digit and a power to find the last digit of the number when raised to the power of 2.")

try:

    power = int(input("Enter a power: "))
    digit = int(input("How many digits: "))

    if power < 0 or digit  < 0:
        raise ValueError("Power must be a positive interger")


    power3 = digit**power
    power4 = power3**2 % 10
    print("result is: ", power4)

except ValueError as error:
    print("Error: ", str(error))




    
    
