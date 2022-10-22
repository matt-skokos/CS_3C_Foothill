def rec_power(a, n):
    # raises 'a' to the int power 'n'
    if n == 0:
        return 1
    else:
        factor = rec_power(a, n // 2)
        if n % 2 == 0:
            return factor * factor
        else:
            return factor * factor * a


print(rec_power(2, 8))
