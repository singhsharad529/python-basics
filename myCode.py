# x = int(input("Enter 1st Number"))
# y = int(input("Enter 2nd Number"))
# z = x + y
# print(z)


# ch = input('enter a char')[0]
# print(ch)


# result = eval(input("Enter an expr"))
# print(result)


# av=5
# x = int(input("How many candies you want"))
# i = 1
# while i <= x:
#     if i>av:
#         print("Our of Stock")
#         break
#     print('Candy')
#     i+=1
#
# print("Bye")


# x=int(input("Enter Number to create n*n pattern"))
#
# for i in range(x):
#     for j in range(x):
#         print("#",end="")
#     print()


y=int(input("Enter rows number to create trianle pattern"))

for i in range(y):
    for j in range(i+1):
        print("#",end="")
    print()

