# map function 
numbers = [1,5,9,4,6,7,5]
squre = map(lambda num:num**2,numbers)
print(numbers)
print("Squre of number",list(squre))

list1 = [1,5,3,4,6]
list2 = [2,8,9,7,6]

addition = map(lambda x,y:x+y,list1,list2)
print(list1)
print(list2)
print("Addition",list(addition))