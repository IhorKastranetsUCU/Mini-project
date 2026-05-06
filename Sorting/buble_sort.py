l1 = [1, 5, 3, 10, 4, 3, 6]

n = len(l1)
for i in range(n):
    for j in range(n-i-1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]
print(l1)