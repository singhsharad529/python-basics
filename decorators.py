# suppose i want to call an function
# but i also want to change some of code
# in a called function
# but i dont have access for this
# to do that suffix part , i can make an decorator
# which does pre taks before calling that function

def div(a, b):
    # i want to swap value
    # if b>a
    # but i dont have access for this
    # this work will be done by decorator
    print(a / b)


# decorator
def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
            return func(a, b)

    return inner


div1 = smart_div(div)
div1(2, 4)
