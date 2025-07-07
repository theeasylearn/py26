import random as r

x= r.random()
print(x)
print("uniform",r.uniform(1,100))
a=10
print("randint",r.randint(a=1,b=10))
print("randrange",r.randrange(start=10,stop=99,step=2))

countries= ("India","usa",'UK','Canada','Australia') 
print(r.choice(countries))
print(r.choices(countries,k=55))

random = [1,2,3,4,5,6,7,8,9,0,'sdddfd','sds','sdf']
print(random)
r.shuffle(random)
print(random)

print("sample",r.sample(random ,k=9))