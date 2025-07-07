"tack age as input if age<18 or age>60 rise error"
try:
    age = int(input("Enter your age when you start job"))
    if age<18 or age>60:
        raise ValueError
    else:
        rage = 60 - age
        print(f"you have {rage} year for do job")
except ValueError:
    print("you are not allow for job")