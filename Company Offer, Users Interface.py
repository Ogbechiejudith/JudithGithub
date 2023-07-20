def company_offer():
    #Judith Company Offer program
    welcome_message = """Welcome to Gcode, your gateway to affordable tech skills.

At Gcode, we believe in empowering individuals like you with top-notch training at budget-friendly prices.
Unlock your potential and join our community of learners today.\n"""

    offer_template = """ \n Dear {},\n
    We at Gcode are excited to offer you an exclusive discount on our tech courses. As a valued customer, 
    we want to support your learning journey and help you acquire valuable skills in the ever-evolving
    tech industry. Don't miss this opportunity to enhance your knowledge and propel your career forward!
    reach us a https://Gcodesupport.com/ for more information on courses offer and much more.\n
    Sincerely,
    Ifechidere,
    Gcode Team.\n"""

    print(welcome_message)
    names = str(input("Enter your name: "))
    company_offer = offer_template.format(names)

    print(company_offer)
    print("Thanks for reaching this website")

company_offer()
