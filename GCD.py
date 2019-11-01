def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


run = True
while run:
    a = input("A: ")
    b = input("B: ")
    print(gcd(int(a), int(b)))
    y_n = input("Finished? y/n: ")

    if y_n == "y":
        run = False

