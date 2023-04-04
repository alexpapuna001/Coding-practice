#https://codeforces.com/contest/1790/problem/C
n = int(input())
for i in range(n):
    x = int(input())
    permlist = []
    ans = []
    for _ in range(x):
        perm = list(map(int,input().split()))
        permlist.append(perm)
    ans = permlist[0]
    for i,j in enumerate(permlist[1]):
        if j not in ans:
            num1 = j
            ind = i
    num2 = permlist[0][ind]
    if num2 in permlist[1]:
        a = permlist[1].index(num1)
        b = permlist[1].index(num2)
        if a>b:
            ans.insert(ind+1,num1)
        else:
            ans.insert(ind,num1)
    else:
        a = permlist[2].index(num1)
        b = permlist[2].index(num2)
        if a>b:
            ans.insert(ind+1,num1)
        else:
            ans.insert(ind,num1)
    
    
    
    print(" ".join(map(str,ans)))
