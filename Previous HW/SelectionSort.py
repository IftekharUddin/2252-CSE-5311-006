def selection_sort(arr):
    array_length = len(arr)

    for i in range(array_length - 1):
        min_index = i  # Assume the first element is the minimum
        
        # Find the minimum element in the remaining unsorted array
        for j in range(i + 1, array_length):
            if arr[j] < arr[min_index]:
                min_index = j  

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == "__main__":
    sample_list = [64, 25, 12, 22, 11]
    print("Unsorted List:", sample_list)
    
    sorted_list = selection_sort(sample_list)
    print("Sorted List:", sorted_list)
