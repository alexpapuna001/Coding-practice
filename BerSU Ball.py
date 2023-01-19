b = int(input())
boys = sorted(list(map(int, input().split())))
g = int(input())
girls = sorted(list(map(int, input().split())))
clone = girls
matches = 0
for i in boys:
    if i-1 in clone:
        matches += 1
        clone.remove(i-1)
    elif i in clone:
        matches += 1
        clone.remove(i)
    elif i+1 in clone:
        matches += 1
        clone.remove(i+1)
print(matches)