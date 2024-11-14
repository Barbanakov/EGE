score = max_sum = 0
f = open('17_37347.txt')
l = [int(i) for i in f]
for i in range (len(l) - 1):
    for j in range (i + 1, len(l)):
        if l[i] * l[j] % 14 != 0:
            score +=1
            max_sum = max(max_sum, l[i] + l[j])
print (score, max_sum)
