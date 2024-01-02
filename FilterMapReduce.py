from functools import reduce


# filter....................
# customize function for filter
def is_even(n):
    return n % 2 == 0


# we can also create lambda

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filter takes two arg: 1. logic and 2. sequence

# evens=list(filter(is_even,nums))
evens = list(filter((lambda n: n % 2 == 0), nums))
print(evens)


# map................
def update(n):
    return n + 2


# doubles = list(map(update, evens))
doubles = list(map(lambda n: n + 2, evens))
print(doubles)


# reduce...............
def add_all(a, b):
    return a + b


# sum = reduce(add_all, doubles)
sum = reduce(lambda a,b:a+b, doubles)

print(sum)


# Experiment with list of dictionary
BOOKS=[
    {'title':'Title One','author':'Author One','category':'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Threee', 'category': 'History'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Six', 'category': 'math'},
]

def findBook(book):
    if book['title']=="Title One":
        return book


my_book=list(filter(findBook,BOOKS))
print(my_book)

