def linear_search(arr, target):
    # Your code here
    # need to traverse the data one item at a time searching for the match meaning in this case:
    # target needsto equal arr[i] ...or arr at a certain index.
    # loop over the arr, checking each item, if true for a target == return the arr[item]
    # if it isn't equal, keep searching for the length of the array.
    for i in arr:
        if target == arr[i]:
            return 1
        else:
            arr[i] += 1

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here

    return -1  # not found
