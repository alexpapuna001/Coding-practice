import math
pi = '3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117'

def main():
    n = int(input())
    for i in range(n):
        count = 0
        x = input()
        for i in range(len(x)):
            if x[i] == pi[i]:
                count += 1
            else:
                break
        print(count)
    
main()
#https://codeforces.com/contest/1790/problem/A