# Polymorphism
#
# 1. Duck Typing
# 2. Operator Overloading
# 3. Method Overloading
# 4. Method Overriding

 # 1. Duck Typing

 # x=5
 # x="Sharad"

class Pycharm:
     def execute(self):
         print("Compiling")
         print("Running")

class MyEditor:
    def execute(self):
        print("spell check")
        print("compiling")

class Laptop:
     def code(self,ide):
         ide.execute()

ide=MyEditor()
# ide=Pycharm()

l1=Laptop()
l1.code(ide)



