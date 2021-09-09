# https://www.slideshare.net/sonickun/rsa-n-ssmjp  ←このサイト様の攻撃手段をpythonコードを含めて自分用にまとめたものです。




1 nが小さい時はfactordbを用いて素因数分解をすることが可能

2 p,qの片方が小さい時も,factordbを用いて素因数分解することが可能

3 p,qの値が近いと,フェルマー法を用いて素因数分解が可能

# Fermat’s factorization method

import math
N = int(input())
x = math.floor(math.sqrt(N)) + 1
y = math.floor(math.sqrt(x**2 - N))
for i in range(10**7):
    w = x**2 - N - y**2
    if w == 0:
        print(x + y, x-y)
        break
    elif w > 0:
        y += 1
    else:
        x += 1

4 p,qが有名な素数だった場合,それをもとに素因数分解することが可能

5 p,qを使い回している場合,  n = p * q , N = p * r とすると, n , N の gcd から p を求めることが可能

6 eの値が小さい時,Low Public Exponent Attackにより,平文 m を得ることが可能

# Low Public Exponent Attack

n = x
e = y #小さい
c = z
while True:
    m, result = gmpy2.iroot(c, e)
    if result == True:
        break
    else:
        c += n
print(long_to_bytes(m))

7 eの値が大きい時,Wieners Attackにより,平文 m を得ることが可能

# Wiener's Attack

import owiener
from Crypto.Util.number import *
n = x
e = y #小さい
c = z
d = owiener.attack(e, n)
print(long_to_bytes(pow(c, d, n)))

8 

9

10

11

12

13

14
