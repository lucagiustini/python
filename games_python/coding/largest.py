def find_largest_number(arr):
    #if not arr:
    #    return None  # Return None if the array is empty

    largest = arr[0]  # Assume the first element is the largest

    for num in arr:
        if num > largest:
            largest = num  # Update the largest number if a larger one is found

    return largest

# Example usage:
my_array = [12, 45, 9, 27, 6, 50]
largest_number = find_largest_number(my_array)
print("The largest number in the array is:", largest_number)