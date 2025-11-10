def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# --- Main program ---
print("Choose search method:")
print("1. Linear Search")
print("2. Binary Search")

choice = input("Enter your choice (1 or 2): ")

# Get array input from user
user_input = input("Enter the array elements (separated by spaces): ")
arr = list(map(int, user_input.split()))
target = int(input("Enter the number to search (from array list): "))

if choice == '1':
    result = linear_search(arr, target)
elif choice == '2':
    arr.sort()
    print("Sorted array:", arr)
    result = binary_search(arr, target)
else:
    print("Invalid choice.")
    result = -1

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
