

#Binary search practice step 1 practice 1
# n, k = list(map(int, input().split()))
# mylist = list(map(int,input().split()))
# quer = list(map(int,input().split()))
# for i in quer:
#     high = n-1
#     low = 0
#     check = True
#     while low <= high:
#         middle = int((high+low)/2)
#         if mylist[middle] == i:
#             print("YES")
#             check = False
#             break
#         elif i > mylist[middle]:
#             low = middle+1
#         elif i < mylist[middle]:
#             high = middle-1
#     if check:
#         print("NO")

#Binary practice step 1 practice 2 and 3
# n, k = list(map(int, input().split()))
# mylist = list(map(int,input().split()))
# quer = list(map(int,input().split()))
# for i in quer:
#     right = n
#     left = -1
#     while left+1 < right:
#         middle = int((right+left)/2)
#         if mylist[middle] < i:
#             left = middle
#         else:
#             right = middle
#     print(right + 1)

#Binary search pratice step 1 problem 4
n = int(input())
m = list(map(int,input().split()))
k = int(input())
for _ in range(k):
    l, r = list(map(int, input().split()))
    count = 0
    for i in m:
        if i >= l and i <=r:
            count+=1
    print(count)








