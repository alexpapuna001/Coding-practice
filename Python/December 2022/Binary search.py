n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
quer = list(map(int,input().split()))


for i in quer:
    h = len(arr)
    l = 0
    bus = True
    while bus:
        # print(arr[int((h+l)/2)],i,l,h)
        if arr[int((h+l)/2)] == i:
            print("YES")
            bus = False
            break
        if arr[int((h+l)/2)] > i:
            # print("hello")
            h = int((h+l)/2)
        if arr[int((h+l)/2)] < i:
            # print("goodbye")
            l = int((h+l)/2)
        if l+1 == h:
            if arr[l] == i or arr[h] == i:
                print("YES")
            else:
                print("NO")
            bus = False
            break
