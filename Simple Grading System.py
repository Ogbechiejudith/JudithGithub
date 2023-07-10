
#Simple Grading System
print("Welcome to Judith Simple Grading System.")
print("Please Enter Score to check Grade.")
while True:
    student = int(input("Enter your Score: "))
    
    if student>= 90:
       print("Your grade is A.")
    elif student >= 80:
        print("Your grade is B.")
    elif student >= 70:
        print("your grade is C.")
    elif student >= 60:
        print("Your grade is D.")
    elif student >= 50:
        print("Your grade is E.")
    else:
        print("Your grade is F:", 'Rewrite the test.')
        print("Another Day to Try Again, Be Positive.")
        

