#https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/A
n,w,h = list(map(int,input().split()))
l = 0
r = n
def good(x):
    return (x//w) * (x//h) >= n
while l + 1 < r:
    m = (r+l) // 2
    if good(m):
        r = m
    else:
        l = m
print(r)