def bubble_sort(arr):
    array_length = len(arr)
    for outer in range(array_length):
        swapped = False  
        for inner in range(0, array_length - outer - 1):  
            if arr[inner] > arr[inner + 1]:  # Swap if elements are in the wrong order
                arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]
                swapped = True
        if not swapped:  
            break

    return arr

if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Unsorted List:", sample_list)

    sorted_list = bubble_sort(sample_list)
    print("Sorted List:", sorted_list)
