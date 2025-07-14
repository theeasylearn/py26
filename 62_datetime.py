from datetime import datetime
# current date and time
now = datetime.now() 
print(now) #now has datetime in Y%M%d H%M%S

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S") # mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S") # dd/mm/YY H:M:S format
print("s2:", s2)
