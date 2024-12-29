def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i + arr[i:].index(min(arr[i:]))  
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = list(map(int, input("Enter numbers to an array ").split()))
selection_sort(arr)
print("Sorted list:", arr)
