import random
import math
# //global list 
alphabets = [
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_symbols = [
'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
'[', ']', '{', '}', ';', ':', "'", '"', ',', '<', '>', '.', '/', '?', '\\', '|', '`', '~'
]

def HashPassword(password):
    print("I will hash this password ",password)

def MatchPassword(HashedPassword,OriginalPassword):
    print(f"I will match {HashedPassword} and {OriginalPassword}")

def GeneratePassword(length=12):
    global alphabets, digits, special_symbols
    # //merge 
    mix = alphabets + digits + special_symbols
    #i will shuffle my list mix 
    random.shuffle(mix)
    MyPassword = [] # empty list     
    size = len(mix) - 1;
    count=1
    length = math.copysign(length,1)
    while count<=length:
        MyPassword.append(mix[random.randint(0,size)])
        count+=1
    return ''.join(MyPassword) #return MYPassword which is list will be return as string    