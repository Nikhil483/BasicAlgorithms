def remove_duplicates(list):
    left,n = 0, len(list)
    if n == 0 or n == 1:
        return n

    for right in range(n-1) :
        if list[right] != list[right +1] :
            list[left] = list[right]
            left += 1  # left here is keeping track where to put the next unique element

    list[left] = list[n -1]
    return left + 1


if __name__ == "__main__" :
    list = [1,2,2,3,3,4,5,5]
    new_length = remove_duplicates(list)

    print(f"Array with duplicates removed - {list[:new_length]}")