# n = int(input())
# for _ in range(n):
#     i , k = input().split() 
#     i = int(i)
#     k = int(k)
#     ans = ""
#     num = 0
#     for _ in range(i):
#         if num<k:
#             ans+=chr(97+num)
#             num+=1
#         else:
#             num=1
#             ans+=chr(97)
#     print(ans)


# n = int(input())
# stud = list(map(int, input().split()))
# stud.sort()
# answer = 0
# for i in range(0, n, 2):
#     answer += stud[i+1]-stud[i]
# print(answer)


# row1 = input().split()
# row2 = input().split()
# row3 = input().split()
# row4 = input().split()
# row5 = input().split()
# ans = 0
# if "1" in row1:
#     ans+=2+abs(row1.index("1")-2)
# elif "1" in row2:
#     ans+=1+abs(row2.index("1")-2)
# elif "1" in row3:
#     ans+=abs(row3.index("1")-2)
# elif "1" in row4:
#     ans+=1+abs(row4.index("1")-2)
# elif "1" in row5:
#     ans+=2+abs(row5.index("1")-2)
# print(ans)

    

    
        

        

    