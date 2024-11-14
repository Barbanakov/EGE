score = max_sum = 0
f = open('17_37337.txt')
l = [int(i) for i in f]
# print(l)
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] % 7 == 0 or l[j] % 7 == 0) and (l[i] % 160 != l[j] % 160):
            score += 1
            max_sum = max(max_sum, l[i] + l[j])
print(score, max_sum)