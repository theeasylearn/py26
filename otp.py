#module to generate otps 
import random 

def getotp(n):
    # if n==0:
    #     print("Invalid Input")
    if n==8:
        return str(random.randint(10000000, 99999999))
    elif n==6:
        return str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
    elif n==4:
        return str(random.randint(10,99)) + str(random.randint(10,99))
    else:
        return "Invalid Input"