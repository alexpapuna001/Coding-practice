n = int(input())
animals = []
for _ in range(n):
    a = int(input())
    animals.append(a)
animals.sort(reverse=True)
suma = 0
ans = 0
if animals[0] > sum(animals[1:]):
    print(1)
else:
    for i in range(1,n):
        suma += animals[i]
        if suma >= animals[0]:
            ans = i+1
            break
    print(ans)
        

