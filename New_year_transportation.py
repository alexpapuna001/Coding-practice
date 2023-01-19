
    
n, t = list(map(int, input().split()))
a = list(map(int, input().split()))
x = 0
while True:
    if x + 1 == t:
        print("YES")
        break
    elif x + 1 > t:
        print("NO")
        break
    else:
        x += a[x]

#https://codeforces.com/problemset/problem/500/A
      