# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # if next item in loop is < cur_i set it to the prev of the cur index
        # if next item in loop is > cur_index set it to thenext of the current index
        # else return the index
        # (hint, can do in 3 loc)

        # if i < cur_index:
        #     #move that shit to the right of the current index, but how.
        # if i > cur_index:
        #     #move that shit to the left of the current index
        # else:
        #     #give me back the list of the sorted array
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[cur_index] > arr[j]:
                cur_index = j
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    return arr


"""
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
"""


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
