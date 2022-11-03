# n= int(input())

# for _ in range(n):
#     t = int(input())
#     arr =  input().split()
#     ans = {}
#     b = 0
#     for i in arr:
#         if int(i) not in ans:
#             ans[int(i)]=0
        
#         ans[int(i)]+=1
#         if ans[int(i)]>1:
#             b=1

#     if b==0:
#         print("yes")
#     else:
#         print("no")
            
# n = int(input())
# # words = []
# arr={}
# for _ in range(n):
#     word = input()
#     if word not in arr:
#         arr[word]= 0
#     else:
#         arr[word]+=1
#     if arr[word] == 0:
#         print("OK")
#     else:
#         print(f"{word}{arr[word]}")
    
# n = int(input())
# ans=0
# arr=[]
# arr.append(0)
# for _ in range(n):
#     ab = input().split()
#     a = int(ab[0])
#     b = int(ab[1])
#     ans-=a
#     if ans < 0:
#         ans=0
#     ans+=b
#     if ans > max(arr):
#         arr.append(ans)
    
# print(max(arr))
    

# from operator import index

# print( input().replace("WUB", " ").lstrip())
n = int(input())
rats = []
women = []
men = []
capitan = []
for _ in range(n):
    member = input().split()
    if member[1] == "rat":
        rats.append(member[0])
    elif member[1] == "woman":
        women.append(member[0])
    elif member[1] == "child":
        women.append(member[0])
    elif member[1] == "man":
        men.append(member[0])
    else:
        capitan.append(member[0])
for i in rats:
    print(i)
for i in women:
    print(i)
for i in men:
    print(i)
for i in capitan:
    print(i)

    


    
    
        

