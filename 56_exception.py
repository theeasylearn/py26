from datetime import datetime
try:
    user_input = input("Enter the date of birth(dd-mm-yyyy)")
    a_date = datetime.strptime(user_input,"%d-%m-%Y")
    if a_date< datetime.today():
        raise ValueError("date should be in future")
    
except ValueError as e:
    print("error",e)
    
else:
    print("date os appointment  is",a_date.strftime("%A %d %B %Y"))
    
finally:
    print("Thank you for using the appointment sheduler")