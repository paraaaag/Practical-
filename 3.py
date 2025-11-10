salaries  = [47000.75, 29000.00, 60000.25, 54000.60, 51000.10, 45000.45, 61000.90]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return  arr
def  bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("# Using selection sort:")
# Using selection sort
selection_sorted = selection_sort(salaries.copy())
print("Salaries sorted using selection sort (ascending):")
print(selection_sorted)
print("Top 5 highest salaries (selection sort):")
print(selection_sorted[-5:][::-1])  # Reverse for highest first
print("\n")
print("# Using bubble sort")
# Using bubble sort
bubble_sorted = bubble_sort(salaries.copy())
print("Salaries sorted using bubble sort (ascending):")
print(bubble_sorted)
print("Top 5 highest salaries (bubble sort):")
print(bubble_sorted[-5:][::-1])
