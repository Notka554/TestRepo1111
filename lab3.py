import sys


b = []
k = ''
a = sys.argv[1]
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

print(b)
out = 0
for j in b:
    out += (1 / j) * 3
print(out)
