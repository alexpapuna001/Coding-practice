n, s, k = list(map(int, input().split()))
f = []
for _ in range(n):
    f.append(int(input()))
f.sort()
ans = 0
mylist = []
cond = True
tracker = []
for i in range(n):
    if i != n-1:
        if f[i+1] - f[i] < s/2:
            cond = False
            break
        elif f[i+1] - f[i] <= k/2:
            tracker.append(i)
        else:
            tracker.append(i)
            mylist.append(f[min(tracker):max(tracker)+1])
            tracker = []
    else:
        tracker.append(i)
        mylist.append(f[min(tracker):max(tracker)+1])
        tracker = []

if cond:
    for i in mylist:
        if len(i) >= 3:
            x = i[1]-i[0]-s/2
            y = i[-1] - i[-2] - s/2
            ans += i[-1]-i[0] + x + y
        elif len(i) == 2:
            ans += (i[1]-i[0])*2
        elif len(i) == 1:
            ans += k
    print(int(ans))
else:
    print(-1)




