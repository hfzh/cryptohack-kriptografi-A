def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = 273246787654
p = 65537

if gcd(a,p)==1:
        print(1)