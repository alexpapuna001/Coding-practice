w = input()
count_c=0
count_l=0
for i in range(len(w)):
    if ord(w[i])>=65 and ord(w[i])<=92 :
        count_c+=1
    else:
        count_l+=1
if count_c>count_l:
    print(w.upper())
else:
    print(w.lower())
        