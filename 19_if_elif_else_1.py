# write a program to accept week day from user (1 to 7) and display day name 
day = input("Enter week day (1 to 7)")
day = int(day)
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("it is not valid day")
    