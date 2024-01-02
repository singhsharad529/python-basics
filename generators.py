# Generators

def topten():
    # yield 1
    # yield 2
    # yield 3
    # yield 4
    # yield 5

    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()

# print(values.__next__())
# print(values.__next__())

for i in values:
    print(i)
