# Method Overiding

class A:
    def show(self):
        print("in a show")


class B(A):

    def show(self):
        print("in b show ")



a1=B()
a1.show()