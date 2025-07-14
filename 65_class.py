# A simple example class 
class Animal: 
	# A sample method 
    def fly(self):
        print("I can fly")
    def eat(self): 
        print("I can eat") 
    def run(self): 
        print("I can run") 
    def sleep(self):
        print("I can sleep")
    
#create object
#object = classname()
Tiger = Animal() #creating object of animal class 
Tiger.eat()
Tiger.run()
Tiger.sleep()

peacock = Animal()  # second object
peacock.fly() # calling method of peacock object