amount = int(input("Enter the value of amount"))

def addmoney():
    global amount
    print("amount before function run",amount)
    amount = amount+1
    print("amount after function run",amount)

addmoney()