f = open('17_37340.txt')
a = [int(i) for i in f]
p = 0
s = 0
for i in range(len(a) - 1):
    for j in range (i + 1, len(a)):
        if ((a[i] - a[j]) % 2 == 0) and (a[i] % 31 == 0 or a[j] % 31 == 0):
            p += 1
            s = max(s, a[i] + a[j])
print(p, s)
