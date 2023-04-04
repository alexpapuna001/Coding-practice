#https://codeforces.com/edu/course/2/lesson/6/1/practice/contest/283911/problem/B

n , k = list(map(int,input().split()))
mylist = list(map(int,input().split()))
queries = list(map(int,input().split()))
for i in queries:
    l = -1
    r = len(mylist) 
    while l + 1 < r:
        m = (l+r)//2
        if mylist[m] > i:
            r = m
        elif mylist[m] < i:
            l = m
        else:
            print(m+1)
            break
        if l+1 == r:
            print(l+1)
            break            
