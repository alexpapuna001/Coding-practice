n=int(input())
my_dict = {}
num = 0
for _ in range (n):
    name = input()
    if name not in my_dict:
        my_dict[name] = 1
        num += 1
print(num)


#https://codeforces.com/problemset/problem/44/A