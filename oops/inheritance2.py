class A:
    def __init__(self):
        print("IN A init")

    def feature1(self):
        print("feature 1")

    def feature2(self):
        print("feature2")


# Single Level inheritance
# B is inheriting from A
class B:
    def __init__(self):
        super().__init__()
        print("IN B init")

    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("feature4")


class C(A,B):

    def __init__(self):
        super().__init__()
        print("in c init")

# print class A init first : from left to right
# same with methods
a1 = C()
