class Lab2Core():
    def Sqrt(self, a):
        c = 1
        c1 = 0
        while (round(c1, 5)) != (round(c, 5)):
            c1 = c
            c = 0.5 * (c + a / c)
        return c
