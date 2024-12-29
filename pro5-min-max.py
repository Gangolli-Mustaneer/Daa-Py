def find_max_min(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    mid = len(arr) // 2
    max1, min1 = find_max_min(arr[:mid])
    max2, min2 = find_max_min(arr[mid:])

    return max(max1, max2), min(min1, min2)

arr = [3, 1, 8, 4, 7, 2, 6, 5]
max_val, min_val = find_max_min(arr)

print("Maximum element:", max_val)
print("Minimum element:", min_val)