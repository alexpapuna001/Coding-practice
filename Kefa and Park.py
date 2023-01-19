n, m = list(map(int, input().split()))
cat = list(map(int, input().split()))
tree = {}
for _ in range(n-1):
    x, y = list(map(int, input().split()))
    if x not in tree:
        tree[x] = [y]
    else:
        tree[x].append(y)
marked = [False] * 10
cons = {}
def dfs(dic, x):
    if x in tree:
        if cat(tree[x] - 1) == 1:
            if tree[x] not in cons:
                cons[tree[x]] = 1
            else:
                cons[tree[x]] += 1           #creates an entry into a dictionary which marks how many consequtive cats the neighbors have encountered 
        marked[x] = True
        for i in tree[x]:
            if not marked[x]:
                dfs(dic,x)
                