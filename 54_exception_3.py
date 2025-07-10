try:
    num1 = int(input("Enter the numerator "))
    num2 = int(input("Enter the denominator "))

    ans = num1/num2
    print("The answer is ", ans)
except ValueError:
    print("Invalid input")
    
except ZeroDivisionError:
    print("Denominator cannot be zero")
    
except Exception as e:
    print("An error occurred: ", str(e))
else:
    
    print("Good By")