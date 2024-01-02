
# Outer Class
class Student:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    # Inner class
    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)


s1=Student('navin',2)
s2=Student('ravi',3)

s1.show()
lap1=s1.lap
lap2=s2.lap

print(id(lap1))
print(id(lap2))

# laptop object
lap1=Student.Laptop()
lap1.show()


