import timeit

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)

def merge(left_half, right_half):
    sorted_array = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left_half) and right_pointer < len(right_half):
        if left_half[left_pointer] < right_half[right_pointer]:
            sorted_array.append(left_half[left_pointer])
            left_pointer += 1
        else:
            sorted_array.append(right_half[right_pointer])
            right_pointer += 1

    sorted_array.extend(left_half[left_pointer:])
    sorted_array.extend(right_half[right_pointer:])

    return sorted_array

array = [5, 2, 4, 7, 1, 3, 2, 6]

execution_time = timeit.timeit(lambda: merge_sort(array), number=1000)
print("Sorted array:", merge_sort(array))
print(f"Execution time over 1000 runs: {execution_time:.6f} seconds")

## Sorted array: [1, 2, 2, 3, 4, 5, 6, 7]
## Execution time over 1000 runs: 0.003142 seconds