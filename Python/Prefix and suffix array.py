n = int(input())
for _ in range(n):
    x = int(input())
    presu = input().split()
    targets = []
    ends = []
    for i in presu:
        if len(i) == x-1:
            targets.append(i)
        if len(i) == 1:
            ends.append(i)
    if targets[0][0:x-2] == targets[1][1:x-1]:
        mystr = targets[1][0]+targets[0]
    else:
        mystr = targets[0][0]+targets[1]
    if mystr[::-1] == mystr:
        print("YES")
    else:
        print("NO")