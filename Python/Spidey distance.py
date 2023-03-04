import math
t, s = list(map(int,input().split()))
n = 1000005
primes = [1]
prime = [True for i in range(n + 1)]
p = 2

MAX_SIZE = 1000001
isprime = [True] * MAX_SIZE
prime = []
SPF = [None] * (MAX_SIZE)
def manipulated_seive(N):
    isprime[0] = isprime[1] = False
    for i in range(2, N):
        if isprime[i] == True:
            prime.append(i)
            SPF[i] = i

        j = 0
        while (j < len(prime) and
               i * prime[j] < N and
                   prime[j] <= SPF[i]):
         
            isprime[i * prime[j]] = False
 
            SPF[i * prime[j]] = prime[j]
             
            j += 1
         
manipulated_seive(1000001)
if s >=3:
    spidey = 2*(s**2)+2*s + 1 + 4*prime[s-4]
elif s == 3:
    spidey = 2*(s**2)+2*s + 1 + 4


else:
    spidey = 2*(t**2)+2*t + 1
taxi = 2*(t**2)+2*t +1
gcd = math.gcd(taxi,spidey)
spidey = int(spidey/gcd)
taxi = int(taxi/gcd)
if taxi%spidey == 0:
    print(f"{int(taxi/spidey)}") 
else:
    print(f"{taxi}/{spidey}")

