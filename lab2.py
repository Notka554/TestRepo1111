def sqrt(a):
    c = 1
    c1 = 0
    while (round(c1, 5)) != (round(c, 5)):
        c1 = c
        c = 0.5 * (c + a / c)
    return c

a_in = input()
a_out = sqrt(float(a_in))
print(round(a_out, 5))
