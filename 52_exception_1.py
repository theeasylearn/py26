try:
    number = int(input("Enter the number to Find qube"))
    if number<0:
        print("number is negative ")
        n= 0-number
        qube = n*n*n
    else:
        qube = number*number*number
    print("qube of number is ",qube)
except ValueError:
    print("Invalid input only number is allowed")