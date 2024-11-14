score = max_sum = 0
f = open('17_37336.txt')
l = [int(i) for i in f]
for i in range(len(l) - 1):
    if (l[i] % 3 == 0) or (l[i + 1] % 3 == 0):
        score += 1
        max_sum = max(max_sum, l[i]+ l[i + 1])
print(score, max_sum)