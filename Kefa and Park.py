n, m = list(map(int, input().split()))
cat = list(map(int, input().split()))
tree = {}
for _ in range(n-1):
    x, y = list(map(int, input().split()))
    if x not in tree:
        tree[x] = [y]
    else:
        tree[x].append(y)
visited = []
ans = 0
print(tree)
def dfs(tree, visited, x, c, cmax):
    global ans
    if x not in visited:
        visited.append(x)
        if cmax > m:
            return
        if x in tree:
            for i in tree[x]:
                if i in tree:
                    if cat[x-1] == 1:
                        if c+1 > cmax:
                            cmax = c+1
                        dfs(tree, visited, i, c+1, cmax)
                    else:
                        dfs(tree, visited, i, 0, cmax)
                            
                else:
                    if cat[x-1] == 1 and cat[i-1] == 1:
                        if cmax < c+2:
                            if c+2 <= m:
                                ans+=1
                        else:
                            if cmax <= m:
                                ans += 1
                    elif cat[x-1] == 0 and cat[i-1] == 1:
                        if cmax < 1:
                            if 1 <= m:
                                ans+=1
                        else:
                            if cmax <= m:
                                ans += 1
                    elif cat[x-1] == 0 and cat[i-1] == 0:
                        if cmax <= m:
                            ans+=1
                    elif cat[x-1] == 1 and cat[i-1] == 0:
                        if cmax < c+1:
                            if c+1 <= m:
                                ans+=1
                        else:
                            if cmax <= m:
                                ans+=1
    else:
        if sum(cat) <= m:
            ans = 1
        else:
            ans = 0
            
                        
                    
                    
            

dfs(tree, visited, 1, 0, 0)
print(ans)

#https://codeforces.com/problemset/problem/580/C
