# def multiply(a,b):
#     return a*b
#
#
# print(multiply(3, 4))


# def is_positive(a):
#     if a > 0:
#         return "it's positive number"
#     else:
#         return "it's not positive number"
#
# print(is_positive(2))

# def reverse_text(a:str):
#     return a
#
# print(reverse_text('python'[::-1]))

# def is_palindrome(a):
#     a = str(a)
#     if a == a[::-1]:
#         return "It's palindrome "
#     else:
#         return "It's not palindrome "
# print(is_palindrome('aziza'))


def list_sum(a):
    total = 0
    for i in a:
        total += i
    print(f"Elementlarning yig‘indisi: {total}")

list_sum([1, 2, 3, 4, 5])
