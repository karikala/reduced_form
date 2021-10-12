def check_prime(n):
    count = 0
    for i in range(2, int(n / 2) + 1):
        if i > 2:
            if n % i == 0:
                count += 1
    if count == 0:
        return True
    else:
        return False


def reduced_form(numer, denomi, Minimum):
    flag = 0
    if numer == 1 or denomi == 1:
        print(str(numer) + " / " + str(denomi))
        flag = 1

    for j in range(2, Minimum):
        if denomi % j == 0 and numer % j == 0:
            denomi = denomi // j
            numer = numer // j
            min = numer if numer < denomi else denomi
            reduced_form(numer, denomi, min)
            if check_prime(numer) and check_prime(denomi):
                print(str(numer) + " / " + str(denomi))
                flag = 1

        if flag == 1:
            return


F = float(input("Enter a number"))
l = len(str(F)) + 1
count = 0
for i in range(l + 1):
    if not isinstance(F, int):
        if F % 1 != 0:
            F = F * 10
            count = count + 1

numerator = int(F)
denominator = 10 ** count

print(numerator, denominator)
if numerator > denominator:
    M = denominator
else:
    M = numerator

print(False and False)

reduced_form(numerator, denominator, M)
print(reduced_form(23, 12, 12))
