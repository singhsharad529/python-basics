# def count(lst):
#     even=0
#     odd=0
#
#     for i in lst:
#         if(i%2==0):
#             even+=1
#         else:
#             odd+=1
#
#     return even,odd
#
#
# lst=[10,2,34,5,23,6,73,34,90]
#
#
# even,odd=count(lst)
#
# print(even,odd)


def userMoreThan5Letters(lst):
    count = 0
    for ls in lst:
        if len(ls) <= 5:
            count += 1
    return count


lst = ['sdfj', 'sdfsdf', 'dsfwer', 'werww']
result = userMoreThan5Letters(lst)
print(result)
