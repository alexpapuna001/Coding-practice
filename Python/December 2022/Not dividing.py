n = int(input())
for _ in range(n):
    x = int(input())
    myarr = list(map(int,input().split()))
    for i in range(1,x):
        if myarr[i-1] == 1:
            myarr[i-1]+=1
        while myarr[i]%myarr[i-1] == 0:
            myarr[i] += 1
    
                
    print(" ".join(list(map(str,myarr))))


