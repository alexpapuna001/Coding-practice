# n = int(input())
# for i in range(n):
#     x = int(input())
#     myarr = list(map(int,input().split()))
#     for i in myarr:
#         my
s = "A man, a plan, a canal: Panama"
newstring = []
s = s.lower()
for i in s:
    if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        print(i)
        newstring.append(i)
pointer1 = 0
pointer2 = len(newstring)-1
print(newstring)
while pointer1 < pointer2:
    if newstring[pointer1] != newstring[pointer2]:
        print(newstring[pointer1],newstring[pointer2],False)
    pointer1+=1
    pointer2-=1
print( True)