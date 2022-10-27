n = int(input("Proszę podać liczbę studentów"))
a = 1
c = 0
while a <= n:
    b = int(input("Proszę podać punkty studenta"))
    c += b
    a += 1
y = c / n
print(y)