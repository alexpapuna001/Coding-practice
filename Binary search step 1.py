n, k = list(map(int, input().split()))
mylist = list(map(int,input().split()))
quer = list(map(int,input().split()))
for i in quer:
    high = n-1
    low = 0
    check = True
    while low <= high:
        middle = int((high+low)/2)
        if mylist[middle] == i:
            print("YES")
            check = False
            break
        elif i > mylist[middle]:
            low = middle+1
        elif i < mylist[middle]:
            high = middle-1
    if check:
        print("NO")
        




