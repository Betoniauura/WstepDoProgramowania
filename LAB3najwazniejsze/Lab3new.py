print("Podaj dwie liczby jedną większą drugą mniejszą:")
x = int(input("Podaj x:"))
y = int(input("Podaj y:"))
if y < x:
    x,y = y,x
while x <= y:
    if x % 2 == 0:
        x += 1
        continue
        print(x, end=" ")
        x += 1
