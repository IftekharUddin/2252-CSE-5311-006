def insertion_sort(arr):

    for next in range(1, len(arr)):  # Start from the second element
        key = arr[next]  
        current = next - 1
        
        # Move elements that are greater than key one position ahead
        while current >= 0 and arr[current] > key:
            arr[current + 1] = arr[current]
            current -= 1
        
        arr[current + 1] = key 

    return arr

if __name__ == "__main__":
    sample_list = [12, 11, 13, 5, 6]
    print("Unsorted List:", sample_list)

    sorted_list = insertion_sort(sample_list)
    print("Sorted List:", sorted_list)
