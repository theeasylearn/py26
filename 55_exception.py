from datetime import datetime
try:
    user_input = input("Enter the date of birth(dd-mm-yyyy)")
    birth_date = datetime.strptime(user_input,"%d-%m-%Y")
    print("date os birth is",birth_date.strftime("%A %d %B %Y"))
except:
    print("Invalid date format. Please use dd-mm-yyyy")
finally:
    print("Thank you for using the date of birth calculator")