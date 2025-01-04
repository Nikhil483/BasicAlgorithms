class MergeSort :

    def merge_sort (self, list) :
        if len(list) > 1 :
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            # Keeps splitting the array until its broken down to individual elements
            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            # Now we start putting them back together
            # This loops runs for the length of the smaller array among left and right
            while i < len(left) and j < len(right) :
                if left[i] < right[j] :
                    list[k] = left[i]
                    i += 1
                else :
                    list[k] = right[j]
                    j += 1
                k += 1

            # Any elements left after last while loop will be appended to end of already sorted array
            # since the array we are copying from is already sorted the sorting wil be preserved
            while i < len(left) :
                list[k] = left[i]
                i += 1
                k += 1

            while j < len(right) :
                list[k] = right[j]
                j += 1
                k += 1


if __name__ == "__main__" :
    sortingObj = MergeSort()
    list = [4,5,7,1,2,9,3,6,8,-1,0]

    sortingObj.merge_sort(list)
    print(list)
