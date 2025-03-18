import random

def partition(arr, low, high):
    pivot = arr[high]  # choosing pivot as the last element
    smaller_element_index = low  # pointer for smaller element
    for current_index in range(low, high):
        if arr[current_index] <= pivot:
            arr[smaller_element_index], arr[current_index] = arr[current_index], arr[smaller_element_index]
            smaller_element_index += 1
    arr[smaller_element_index], arr[high] = arr[high], arr[smaller_element_index]
    return smaller_element_index  # pivot's final position

def quickselect(arr, low, high, i):
    if low == high:
        return arr[low]

    pivot_index = random.randint(low, high)  # random pivot selection
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # swap pivot with last element
    
    pivot_final = partition(arr, low, high)
    num_elements_in_left_partition = pivot_final - low + 1  # number of elements in left partition (including pivot)

    if i == num_elements_in_left_partition:
        return arr[pivot_final]  # found the i-th smallest element
    elif i < num_elements_in_left_partition:
        return quickselect(arr, low, pivot_final - 1, i)  # search left
    else:
        return quickselect(arr, pivot_final + 1, high, i - num_elements_in_left_partition)  # search right


arr = [7, 10, 4, 3, 20, 15]
i = 3  # find the 3rd smallest element
result = quickselect(arr, 0, len(arr) - 1, i)
print(f"{i}-th smallest element is {result}")
