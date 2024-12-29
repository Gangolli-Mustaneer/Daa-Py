def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [3, 1, 8, 4, 7, 2, 6, 5]
print("Sorted list:", quick_sort(arr))