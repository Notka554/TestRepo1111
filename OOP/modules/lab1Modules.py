class Lab1Core():
    def Calculate(self, a1, b1, z1):
        if z1 == '+':
            a1 += b1
            return a1
        elif z1 == '-':
            a1 -= b1

        elif z1 == '/':
            a1 /= b1

        elif z1 == '*':
            a1 *= b1

        elif z1 == '^':
            a1 **= b1
        assert isinstance(a1, object)
        return a1
