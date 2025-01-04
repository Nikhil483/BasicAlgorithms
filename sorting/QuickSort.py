max_depth = 0
from time import time
import random

def hoares_partition(list, low, high):
    pivot = list[low]
    left,right = low-1, high+1

    while True:
        # Move the left index to the right util we find element larger than pivot
        # this will give ascending order
        # to get desc order, flip the signs on both while loops.
        left += 1
        while list[left] < pivot :
            left += 1

        # Move the right index to the left util we find element smaller than pivot
        right -=1
        while list[right] > pivot :
            right -= 1

        # if the pointers cross over or meet, then pointer right is the index where pivot sits

        # key point to note is that pivot and right are not swapped here,
        # this just tells where to cut/partition the array,
        # so we proceed by considering pivot part of the left partition in quicksort method
        if left >= right :
            return right

        list[left], list[right] = list[right], list[left]

def quick_sort_using_hoare_algo(list, low, high, depth = 0):
    global max_depth
    max_depth = max(max_depth, depth)

    if low < high :
        pivot = hoares_partition(list,low,high)
        quick_sort_using_hoare_algo(list, low, pivot, depth + 1)  # not pivot-1 because pivot and right were not swapped,
                                                                  # pivot will be part of the left partition
        quick_sort_using_hoare_algo(list, pivot + 1, high, depth + 1)

if __name__ == "__main__":

    # list_unique_elements = [3,6,9,1,0,5,-7,2,7,4, 78,-35,67,100,456,456,123,23,-67,-56,-1,85,-444,-666,-676,1234,5678,11,23,56,78]

    max_depth = 0
    length = 1000

    list_unique_elements = [random.randint(0, 10000) for _ in range(length)]

    start_time = time()
    quick_sort_using_hoare_algo(list_unique_elements, 0, len(list_unique_elements) - 1)
    end_time = time()

    execution_time = (end_time - start_time) * 1000

    # print("Sorted list : " + str(list_unique_elements))
    print("Max-depth : " + str(max_depth))
    print(f"Time taken : {execution_time:.2f} milliseconds")
