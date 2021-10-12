def main():
    F = float(input("Enter a number"))
    l = len(str(F)) + 1
    count = 0
    for i in range(l + 1):
        if not isinstance(F, int):
            if F % 1 != 0:
                F = F * 10
                count = count + 1

    num = int(F)
    denom = 10 ** count
    return num, denom


def _gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x == y:
        return x
    if x > y:
        return _gcd(x - y, y)
    return _gcd(y, y - x)


def reduced_form(x, y):
    z = _gcd(x, y)
    up = x // z
    down = y // z
    return str(up) + "/" + str(down)


if __name__ == "__main__":
    x, y = main()
    print(reduced_form(x, y))
