#https://codeforces.com/group/yQ3W2TUEr9/contest/430015/problem/A
q = int(input())
for i in range(q):
    n = int(input())
    count2 = 0
    count3 = 0
    count5 = 0
    while n%2 == 0:
        n//=2
        count2 += 1
    while n%3 == 0:
        n//=3
        count3 += 1
    while n%5 == 0:
        n//=5
        count5 += 1
    if n == 1:
        print(count2+count3*2+count5*3)
    else:
        print(-1)
    
