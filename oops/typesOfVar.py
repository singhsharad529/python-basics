
# In memory:
# there are two type of namespace
# Namespace is an area where we create object or variables
# 1. Class Namespace
# 2. Instance Namespace


class Car:
    # class variable
    wheels=4

    def __init__(self):
        self.mil=10
        self.com="bmw"

c1=Car()
c2=Car()

c1.mil=8

Car.wheels=5


print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
