# create an array
# find the largest number in the array

array = [1, 2, 3, 4, 15, 6, 7, 8, 9]

def find_largest():
    largest = array[0]
    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]
    print(largest)

find_largest()