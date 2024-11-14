score = max_sum = 0
f = open('17_37341.txt')
l = [int(i) for i in f]
# print(l)
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] % 19 == 0 or l[j] % 19 == 0) and (l[i] - l[j]) % 2 == 0:
            score += 1
            max_sum = max(max_sum, l[i] + l[j])
print(score, max_sum)
