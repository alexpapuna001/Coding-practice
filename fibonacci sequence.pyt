#fibonacci sequance with dynamic programming


def fibo(n, memo = {}):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
x = int(input())
print(fibo(x))
        