#membership operator
#returns true if the element is present in the list
x =int(input("Enter the value of x "))
print("x in list",x in [1, 2, 3, 4, 5])
print("x not in list",x not in [1, 2, 3, 4, 5])

fruit = ['banana','kiwi','orange','apple']
isfound = input('Enter your faviourate fruit ')
print(isfound in fruit)  # True
print(isfound not in fruit)  # False

city ="Bhavnagar Surat Botad"
isfound = input('Enter your city name ')
print(isfound in city)  # True
print(isfound not in city)  # False