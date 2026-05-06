def merge(a, b):
    n = len(a)
    m = len(b)
    c = [0] * (n + m)

    i = 0
    j = 0
    k = 0

    while i < n or j < m:
        if i < n and j < m:
            if a[i] <= b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
            k += 1
        elif i < n:
            c[k] = a[i]
            i += 1
            k += 1
        else:
            c[k] = b[j]
            j += 1
            k += 1

    return c

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)


l1 = [1, 5, 3, 10, 4, 3, 6]
res = merge_sort(l1)

print(res)