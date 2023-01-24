n, m = list(map(int,input().split()))
ans = 0
def func(x, y):
    global ans
    if x == y:
        return
    elif x > y:
        ans += int(x-y)
    elif x < y:
        if y%2 == 1:
            ans+=2
            func(x, (y+1)/2)
        else:
            ans+=1
            func(x, y/2)
func(n,m)
print(ans)


#https://codeforces.com/problemset/problem/520/B