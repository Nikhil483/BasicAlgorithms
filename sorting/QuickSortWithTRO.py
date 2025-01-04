from QuickSort import hoares_partition
from time import time
import random

max_depth = 0

# variable depth is only to compare depth, insignificant to algorithm itself
def quick_sort_with_TRO_and_hoares_partition(list, low, high,depth = 0):
    global max_depth
    while low < high:
        max_depth = max(max_depth, depth)
        pivot = hoares_partition(list, low, high)

        if pivot - low < high - pivot :
            quick_sort_with_TRO_and_hoares_partition(list, low, pivot, depth +1)
            low = pivot + 1
        else :
            quick_sort_with_TRO_and_hoares_partition(list, pivot+1, high, depth+1)
            high = pivot


if __name__ == "__main__":

    # list_unique_elements = [3,6,9,1,0,5,-7,2,7,4, 78,-35,67,100,456,456,123,23,-67,-56,-1,85,-444,-666,-676,1234,5678,11,23,56,78]
    max_depth = 0

    length = 1000
    list_unique_elements = [random.randint(0, 10000) for _ in range(length)]

    start_time = time()
    quick_sort_with_TRO_and_hoares_partition(list_unique_elements, 0, len(list_unique_elements) - 1)
    end_time = time()

    execution_time = (end_time - start_time) * 1000

    # print("Sorted list : " + str(list_unique_elements))
    print("Max-depth : "+ str(max_depth))
    print(f"Time taken : {execution_time:.2f} milliseconds")
