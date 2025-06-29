#write a program to print following pattern 
# 1     8       27      64      125         .... 10000
# 1     2        3       4        5          
'''
    steps 
    1) create variable num, qube
    2) num = 1
    3) qube = num * num * num 
    4) display qube 
    
    5) num = num + 1
    6) qube = num * num * num 
    7) print qube 
    
    8) num = num + 1
    9) qube = num * num * num 
    10) print qube 
    
    steps are repeative therefore we will not write further  
'''
num = 1 
qube = 0 

while qube<9261:
    qube = num * num * num 
    print(qube,end=' ')
    num = num + 1

print("")
print("Good bye")