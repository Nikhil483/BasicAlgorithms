from QuickSort import hoares_partition

def findKthLargest(list, low, high, k, n) :

    if low <= high :
        pivot = hoares_partition(list, low, high)

        target_index = n - k
        if pivot == target_index :
            return list[pivot]
        elif pivot > target_index :
            # since we are already checking pivot equals k-1, in the left partition we should only look until pivot -1
            return findKthLargest(list, low, pivot-1, k, n)
        elif pivot < target_index :
            return findKthLargest(list, pivot + 1, high, k, n)


if __name__ == "__main__" :
    list = [7,8,5,1,4,3,6,9,2]
    k = 2
    n = len(list)
    print(findKthLargest(list, 0, n - 1, k, n))