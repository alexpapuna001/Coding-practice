"""return a value that is the sum of all non negative integers before the number n"""
# a = int(input())
# def factorial(n):
#     if n>=0:
#         return n + factorial(n-1)
#     else:
#         return 0
# print(factorial(a))


"""counts how many unique paths exist from top right corner of an n x m grid to the bottom left corner. We can only move down or right"""
# x = int(input())
# y = int(input())
# def grid(n, m):
#     if n == 1 or m == 1:
#         return 1
#     return grid(n-1,m) + grid(n,m-1)
# print(grid(x, y))

"""write a code that counts how many ways we can partition n objects using parts up to m"""
x = int(input())
y = int(input())
def partition(n, m):
    if n == 0:
        return 1
    if m == 0 or n < 0:
        return 0
    return partition(n-m, m) + partition(n, m-1)
print(partition(x,y))