# x = "PDP \a\a\a\a\a"
#
# print(x)
#
# a = "PDP school \f\f\f\f"
#
# print(a)
#
# b = "PDP \rschool"
#
# print(b)
#
# d = "PDP\tschool"
#
# print(d)
#
# m = "PDP \v school"
#
# print(m)
#
# n = "PDP \0"
#
# print(n)


x = int(input("x:"))

b = int(input("b:"))

n = int(input("b:"))

if x and b and n:
    if x > b > n:
        print(n)
    elif x > b < n:
        print(b)

    elif x< b < n:
        print(b)
    elif x > b > n:
        print(b)
    else:
        print(x)

