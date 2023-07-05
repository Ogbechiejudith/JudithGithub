

#SIMPLE USER INTERFACE PRINT FUNCTION

print("CONVERT YOUR WEIGHT IN KILOGRAM TO POUND: ")
weight = eval(input("ENTER YOUR WEIGHT IN KILOGRAM: "))
p_weight = weight * 2.2
print("Your weight in pound is: ", p_weight )


print("ENTER THREE NUMBER TO KNOW THE SUM AND AVERAGE OF THE NUMBER.")
num1 = int(input("ENTER THE FIRST NUMBER: "))
num2 = int(input("ENTER THE SECOND NUMBER: "))
num3 = int(input("ENTER THE THIRD NUMBER: "))
total = num1*num2*num3
average = total/2
print("Your number is ", total)
print("And the average is ",  average)


#TIP CALCULATOR
print("ASK THE USER FOR THE PRICE OF THE MEAL AND PERCENT TIP , THEN CALCULATED THE TOTAL.")
print("THANK FOR BUYING FROM US.")
customer = eval(input("PLEASE ENTER THE PRICE OF THE MEAL: "))
tip = eval(input("AMOUNT OF TIP GIVEN: "))
total = customer + tip
print("Your tip is: ", tip)
print("Total bill is: ", total)

