# n = list(input())
# my_dict = set()
# answer = 0 
# for i in n:
#     my_dict.add(i)
# if len(my_dict) % 2 == 1:
#     print("IGNORE HIM!")
# else:
#     print("CHAT WITH HER!")
    

# n= int(input())
# for i in range(n):
#     word = input()
#     n = list(word)
#     my_dict = list()
#     for j in n:
#         my_dict.append(ord(j))
#     my_dict = sorted(my_dict)
#     a=1
#     for j in my_dict[0:len(my_dict)-1]:
#         if my_dict[my_dict.index(j)] + 1 == my_dict[my_dict.index(j)+1]:
#             a=a*1
#         else:
#             a=a*0
#     if a == 1:
#         print("YES")
#     else:
#         print("NO")
        
# n = int(input())
# nums = input().split()
# even_num = []
# odd_num = []
# for i in nums:
#     if int(i) % 2 == 1:
#         odd_num.append(int(i))
#     else:
#         even_num.append(int(i))

# if len(odd_num) + 1 == len(even_num):
#     print(0)
# elif len(even_num) + 1 == len(odd_num):
#     print(0)
# elif len(even_num)  == len(odd_num):
#     print(0)
# elif len(odd_num) > len(even_num) :
#     for _ in range(len(even_num)+1):
#         odd_num.remove(max(odd_num))
#     print(sum(odd_num))
# elif len(even_num) > len(odd_num) :
#     for _ in range(len(odd_num)+1):
#         even_num.remove(max(even_num))
#     print(sum(even_num))

# n = int(input())       
# f = input().split()
# nums = []
# for i in f:
#     nums.append(int(i))
# nums_a = list()
# nums_d = list()
# n_a = 0
# n_d = 0
# for _ in nums:
#     print(max(nums))
#     print(max(nums) not in nums_d)
#     print(max(nums) in nums_d)
#     if max(nums) not in nums_d:
#         nums_d.append(nums.pop(nums.index(max(nums))))
#         print(nums_d)
#         n_d += 1
#     elif max(nums) in nums_d:
#         n_a += 1
#         nums_a.insert(0 , nums.pop(nums.index(max(nums))))
#         print(nums_a)
# if len(nums) == 0:
#     print("YES")
#     print(len(n_a))
#     print(n_a)
#     print(len(n_d))
#     print(n_d)
# else:
#     print("NO")



    


    


    



