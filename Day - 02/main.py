# Day 02 exercice : Tip Calculator

# First we need to present the program and make somes inputs
welcome_message_to_program = print("Welcome to the tip calculator.")

bill_amount = input("What was the total bill ? $")
how_many_people = input("How many people to split the bill ? ")
percentage_tip = int(input("What percentage tip would you like to give ? \n10, 12, 15 or 20 : "))


result_bill_divided = float(bill_amount) / int(how_many_people)

if percentage_tip == 10:
    final_result = result_bill_divided * 1.1
    print(f"Each person should pay : ${round(final_result, 2)}")
elif percentage_tip == 12:
    final_result = result_bill_divided * 1.12
    print(f"Each person should pay : ${round(final_result, 2)}")
elif percentage_tip == 15:
    final_result = result_bill_divided * 1.15
    print(f"Each person should pay : ${round(final_result, 2)}")
elif percentage_tip == 20:
    final_result = result_bill_divided * 1.2
    print(f"Each person should pay : ${round(final_result, 2)}")
else:
    print(f"Your {percentage_tip} is not valid.")