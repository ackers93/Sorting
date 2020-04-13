# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for x in range(i + 1, len(arr)):
            if(arr[x] < arr[smallest_index]):
                smallest_index = x

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)

    # loop through array
    for i in range(n):
        for x in range(0, n-i-1):

            # swap if smaller than previous element
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
