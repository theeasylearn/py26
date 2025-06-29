#write a program to print following pattern 
#1  3   5   7   9   11  13  15  17  19  ... 1000
'''
    steps 
    ------------------------------------
    create variable count 
    store 1 into count 
    
    print count
    count = count + 2
    
    print count 
    count = count + 2
    
    print count
    count = count + 2
    
    print count 
    count = count + 2
    
    print count 
    count = count + 2
    above steps are repatative therefore we will not steps further 
'''
count = 1
while count<=1000: #< > <= >=
    print(count,end=' ')
    count = count + 2

