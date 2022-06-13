def insertion_sort(arr):
    indexing_length = range(1, len(arr))
    for i in indexing_length: # Iterates from the second element  
        value_to_sort = arr[i] # to the last element.

        # Iterates the list to the left and checks if we need to do any 
        # swaps and stops if we don’t need to do anymore swaps.
        # Checking if the left neighbour is bigger than the current element. 
        # i must be greater than 0 as there is no -1th entry in the list. 
        while arr[i-1] > value_to_sort and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i = i -1



# Funtion used to call Quicksort in the Benchmark app
def quicksort(arr):
    quicksort_algo(arr, 0, len(arr) - 1)


# Check whole array from index 0
def quicksort_algo(arr, left, right):
    if left < right: # Base case - If sun-array is 1
        partition_pos = partition(arr, left, right)
        # Call quicksort_algo recursively
        quicksort_algo(arr, left, partition_pos -1)
        quicksort_algo(arr, partition_pos + 1, right)

# Returns the index of the pivot element after the first step of Quicksort
def partition(arr, left, right):
    i = left
    j= right - 1
    pivot = arr[right]

    # Checks the condition where i and j cross
    while i < j:
        # while i is not at end of array & the element at index i is less than pivot, increase i
        while i < right and arr[i] < pivot:
            i += 1 # Move right
        # check if j is greater than left and if element at index j is greater than the pivot
        while j > left and arr[j] >= pivot:
            j -= 1 # Move left
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # Check if i and j have crossed yet
    if arr[i] > pivot:
        # If not, swap as below
        arr[i], arr[right] = arr[right], arr[i]

    # i determines where to split the array
    return i

def counting_sort(ary):
    size = len(ary)
    output = [0] * size
    # Create and initialize count array
    count = [0] * 101
    # Keep track of how many of each variable there are.
    for no in range(0, size):
        count[ary[no]] += 1
    # Keep track of the total number of count
    for no in range(1, 101):
        count[no] += count[no - 1]
    # In the count array, find the index of each member of the original array.
    # and place the elements in output array
    no = size - 1
    while no >= 0:
        output[count[ary[no]] - 1] = ary[no]
        count[ary[no]] -= 1
        no -= 1
    # Copy the sorted elements into original array
    for no in range(0, size):
        ary[no] = output[no]

def merge(a1,a2):
    c=[] # Mergerd array
    x=0 # Keep track of leftmost element in left array
    y=0 # Keep track of leftmost element in right array

    # Compares the left index at index x with the right array at index y
    while(x<len(a1) and y<len(a2)):
        if(a1[x]<a2[y]):
            c.append(a1[x])
            x+=1
        else: # Right array is smaller than the left array or they are equal
            c.append(a2[y])
            y+=1
    # Transfer every element from left array to merged array w/o 
    # considering right array
    while(x<len(a1)): 
        c.append(a1[x])
        x+=1
    # Every element from left array is already sorted but there are 
    # some missing elements of the right array
    while(y<len(a2)):
        c.append(a2[y])
        y+=1
    return c

def mergesort(array):
    if(len(array)==1): # Base Case
      return array
    mid=(len(array))//2
    # 2 recursive sub arrays
    a1=mergesort(array[:mid]) # beginning or array to mid-point
    a2=mergesort(array[mid:]) # mid-point to end of the array
    return merge(a1,a2) # perform merge function

def bubble(arr):
    indexing_length = len(arr) - 1 # Can not apply comparision starting with last item of list (Ther is no number after the last number in the array so we can’t do a comparison)
    sorted = False # Create variable of sorted and set it equal to false. Used tobreak out of the while loop when the array is sorted

    while not sorted:  # Repeat until sorted = True
        sorted = True  # Break out of the while loop whenever we have gone through all the values

        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]: # if there is an item to the left is greater than the item to its right, say that the sorted variable is false, and then flip those two items
                sorted = False # These values are unsorted
                arr[i], arr[i+1] = arr[i+1], arr[i] # Swap these values
    return arr # Return the now sorted array.

