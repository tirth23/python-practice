noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in noprimes]
print(primes)

from math import sqrt
n = 200
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)}
print(no_primes)