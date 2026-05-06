l1 = [1, 5, 3, 10, 4, 3, 6]
n = len(l1)

for i in range(n):
    small_index = i
    for j in range(i, n):
        if l1[j] < l1[small_index]:
            small_index = j
    l1[i], l1[small_index] = l1[small_index], l1[i]

print(l1)