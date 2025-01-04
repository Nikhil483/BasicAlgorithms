class FindElement :
    def binary_search (self, list, element_to_find) :

        low, high  = 0, len(list) - 1

        while low <= high :
            mid  = low + (high - low) // 2
            if list[mid] == element_to_find :
                return mid
            elif list[mid] < element_to_find :
                low = mid + 1
            else :
                high = mid - 1

        return -1

if __name__ == "__main__" :
    list = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    element_to_find = 8
    findElement = FindElement()

    index = findElement.binary_search(list, element_to_find)
    if index == -1 :
        print(f"{element_to_find} was not found")
        exit()
    print(f"{element_to_find} was found at index {index} in array {list}")