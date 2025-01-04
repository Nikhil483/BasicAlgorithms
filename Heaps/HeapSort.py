from Heaps.MinHeapImpl import MinHeap


def heap_sort(list):
    mh = MinHeap()
    for ele in list:
        mh.insert(ele)

    sorted_list = []
    while mh.getLen() > 0 :
        sorted_list.append(mh.extract_min())

    return sorted_list

if __name__ == "__main__" :

    unsorted_list = [1,-5, 6, 7, 2, 0, 3]
    print("Original list : "+ str(unsorted_list))
    print("Sorted list : " + str(heap_sort(unsorted_list)))