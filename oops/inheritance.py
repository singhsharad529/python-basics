
class A:
    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature2")

# Single Level inheritance
# B is inheriting from A
class B(A):
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature4")

# Multilevel inheritance
class C(B):
    def feature5(self):
        print("feature 5") 


a1 =A()

a1.feature1()
a1.feature2()

b1 =B()

b1.feature1()

c1 =C()
c1.feature3()
