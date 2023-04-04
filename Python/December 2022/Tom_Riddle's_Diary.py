n=int(input())
my_dict = {}
for _ in range (n):
    name = input()
    if name in my_dict:
        print("YES")
    else:
        my_dict[name] = 1
        print("NO")

#https://codeforces.com/problemset/problem/855/A