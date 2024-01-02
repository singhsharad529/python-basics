

class Computer:
    def __init__(self):
        self.name="sharad"
        self.age=13

    def update(self):
        self.name="rohit"

    def compare(self,other):
        if self.age==other.age:
            return True



c1=Computer()
c2=Computer()

c1.update()
print(c1.name)
print(c2.name)


print(id(c1))
print(id(c2))

#...............comparison
if c1==c2: # comparing two address
    print("They are same")

if c1.compare(c2):
    print("they have same values")
