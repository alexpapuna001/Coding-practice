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
def dfs(tree, visited, x, c):
    global ans
    if x not in visited:
        if cat[x-1] == 1:
            c += 1
        else: 
            c = 0
        visited.append(x)
        for i in tree[x]:
            if c>m:
                if i in tree:
                    dfs(tree, visited, i, c)
                else:
                    if cat[i-1] == 1:
                        c += 1
                    else:                         
                        c = 0
                    if c<=m:
                        ans += 1
            

dfs(tree, visited, 1, 0)
print(ans)

