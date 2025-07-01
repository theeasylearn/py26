# write a program to calculate compound interest of given amount, rate, year 
'''
    steps
    1) create variable amount, rate, year, interest 
    2) accept amount from user 
    3) accept rate from user 
    4) accept year from user 
    
    5) calculate interest for 1st year 
       interest = (amount * rate * 1) / 100
    6) add interest into amount 
       amount = amount + interest
    
    7)  calculate interest for 2nd year
     interest = (amount * rate * 1) / 100
    8) amount = amount + interest 
       above code is repetative so we do not write code further 

'''
amount = 0 
rate = 0 
year = 0 
interest = 0 
amount = int(input("Enter amount"))
rate = int(input("Enter rate"))
year = int(input("Enter amount"))
count=0;
original_amount = amount
while count<year:
    interest = (amount * rate * 1) / 100
    amount = amount + interest
    count=count+1
interest = amount - original_amount
print(f"total interest = {interest} ")