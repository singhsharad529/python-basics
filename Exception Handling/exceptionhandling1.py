# Errors
#     1. Compiler Time
#     2. Logical
#     3. Run Time

a=5
b=9

try:
    print("resource open")
    print(a/b)

    k=int(input())
    print(k)
except ZeroDivisionError as e:
    print("You can't divide a number by zero ",e)
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("Something went wrong",e)

finally:
    print("resource closed")
