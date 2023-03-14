ch = ""
while True:
    n = int(input("Donner un entier : "))
    if 0 <= n < 10000:
        break
if n != 0:
    for i in range(n):
        ch += '('
    for i in range(n):
        ch += ')'
else:
    ch = '.'
print(ch)
