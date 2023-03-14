def degpow(n, p):
    ch = str(n)
    s = 0
    for i in range(len(ch)):
        s += int(ch[i])**p
        p += 1
    k = s / n
    if type(k) == int:
        return k
    else:
        return -1

n = int(input("Donner un entier positif : "))
while n <= 0:
    n = int(input("Donner un entier positif : "))

p = int(input("Donner un entier positif : "))
while p <= 0:
    p = int(input("Donner un entier positif : "))

k = degpow(n, p)
print(k)
