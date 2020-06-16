def linear_search(arr, target):
    # Your code here
    # need to traverse the data one item at a time searching for the match meaning in this case:
    # target needsto equal arr[i] ...or arr at a certain index.
    # loop over the arr, checking each item, if true for a target == return the arr[item]
    # if it isn't equal, keep searching for the length of the array.

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # what is a binary search?
    # a search that uses sorted elements by ignoring half
    # ie: if its > go to the right if its < go to the left
    # if x matches the middle return the mid index
    # if the taret is less than the item go to the left.
    # elif the target is greater than the item go to the right.
    # ^ complete this each time you need to to have it narrow down the search until it finds the item.
    # else return target.

    # Your code here
    # set the high and low of the target.
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (
            high + low
        ) // 2  # this finds the mid point between the high end and low end.
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    else:

        return -1  # not found
