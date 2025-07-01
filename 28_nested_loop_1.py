# write a program to print 1 to 5 muliplication table 
'''
    create number store 1 into it 
    create multiplier store 1 into it 
    
    result = number * multiplier 
    print number X multiplier = result 
    
    multiplier = multiplier + 1 
    result = number * multiplier 
    print number X multiplier = result
    
    multiplier = multiplier + 1 
    result = number * multiplier 
    print number X multiplier = result 
    
    here steps are repatative hence we will write code further.
    
'''
number = 1
multiplier = 1
while number<6: #outer loop
    while multiplier<11: #inner loop
        result = number * multiplier
        print(f"{number} X {multiplier} = {result}")
        multiplier = multiplier + 1 

    number=number+1
    multiplier=1

