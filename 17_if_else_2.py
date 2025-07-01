# write a program to convert 24 hours format time into 12 hours format 
# accept hours from user 
hours = input("Enter hours in 24 hours format") # 22
#convert hours into integer 
hours = int(hours)
# 18 hours
if hours>12:
    hours = hours - 12 
    print(f"{hours} PM")
else:
    print(f"{hours} AM")
print("Good Bye.")