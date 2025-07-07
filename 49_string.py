name = "We are learning python the easy learn academy our batch code is 26"
print(name)
print("length is",len(name))
name="py 26"
print("isalnum",name.isalnum())
print("isalpha",name.isalpha())
print("isnumeric",name.isnumeric())
print("islower",name.islower())
print("isupper",name.isupper())
print("isspace",name.isspace())
print("length is",len(name))
print(f"Welcome to {name.upper()}!")


print(f"Welcome to {name.lower()}!")
name = "We are learning python the easy learn academy our batch code is 26"
print(f"Welcome to {name.title()}!")
list = ('we','are','learning','python')
a = ','.join(list)
print(a)
b = a.split()
print(b)
c= a.split(',')
print(c)
line = "India is a country where India’s diversity, India’s culture, India’s history, and India’s unity are celebrated."
print(line)
x = line.replace('India','Bharat')
print(x)

y =line.replace("India",'Bharat',3)
print(y)

z= line.split()
print(z)