n = int(input())
s = list(map(int, input().split()))
police = 0
cases = 0
for i in s:
    if i > 0 :
        police += i
    if i == -1:
        if police == 0:
            cases+=1
        else:
            police -=1
print(cases)
            
            
#https://codeforces.com/problemset/problem/427/A