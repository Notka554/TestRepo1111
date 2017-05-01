import sys


class Lab3Core():
    def Calculate(self):
        b = []
        k = ''
        a = sys.argv[0]
        l = len(a)
        q = 0
        for i in a[7:]:
            q += 1
            if q == l:
                k = k + i
                b.append(float(k))
                break
            if i == ',':
                b.append(float(k))
                k = ''
            else:
                k = k + i

        out = 0
        for j in b:
            out += (1 / j) * 3
        self.Poly = b
        return out
