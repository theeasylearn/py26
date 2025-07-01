# write a program to convert 24 hours format time into 12 hours format 
# accept hours from user 
hours = input("Enter hours in 24 hours format") # 22
#convert hours into integer 
hours = int(hours)
# 18 hours
#check hours are in valid range or not (1 to 24)
#   25<0 or 25>24
if hours<0 or hours>24:
    print("invalid hours ")
else:
    if hours>12:
        hours = hours - 12 
        print(f"{hours} PM")
    else:
        print(f"{hours} AM")
# if hours>0 and hours<25:
#     if hours>12:
#         hours = hours - 12 
#         print(f"{hours} PM")
#     else:
#         print(f"{hours} AM")
# else:
#     print("invalid hours ")
print("Good Bye.")