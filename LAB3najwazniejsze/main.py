x = -4
while x <= 4:
    if -2 <= x <= 2:
        x = x + 0.5
        continue
    y = 2*x**2 -5*x -8
    print(f"f({x}) = {y}")
    x = x + 0.5

print("koniec", x)

