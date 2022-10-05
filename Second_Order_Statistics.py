n = int(input())
nums = input().split()
my_set = set()
for i in nums:
    my_set.add(int(i))
lowest=min(my_set) 
if len(my_set) < 2:
    print("NO")
else:
    answer = max(my_set)
    for i in my_set:
        if i > lowest and i < answer :
            answer = i
    print(answer)

#https://codeforces.com/problemset/problem/22/A


        



    
    
    



