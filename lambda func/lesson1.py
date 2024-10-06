# high_ord_func = lambda x,func: x + func(x)
#
# print(high_ord_func(2, lambda x: x * x))
#
# print(high_ord_func(2, lambda x: x + 3))


number = [10,9,8,7,6,5,4,3,2,1]
juft = list(filter(lambda number: (number % 2 == 0), number))  # noqa
toq = list(filter(lambda number: (number % 2 == 1), number))  # noqa
print(sorted(juft))
print(sorted(toq))
