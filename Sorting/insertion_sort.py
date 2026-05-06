l1 = [1, 5, 3, 10, 4, 3, 6]
n = len(l1)

for i in range(1, n):
    j = i-i
    key = l1[i]
    while j >= 0 and l1[i] > key:
        l1[j+1] = l1[j]
        j-= 1
    l1[j+1] = key

print(l1) 