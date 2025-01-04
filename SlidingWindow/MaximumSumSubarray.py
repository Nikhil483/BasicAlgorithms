def maximum_sum_sub_array_with_indices (list) :
    max_sum_subarray = list[0] # stores max sum calculated so far
    curr_sum, left, right, possible_start = 0, 0, 0, 0
    # possible_start stores the index of element which is considered after there is negative curr_sum so far

    for i in range(len(list)) :
        if curr_sum < 0 :
            curr_sum = 0
            # if sum so far is -ve we can set it to Zero, later the item of the iteration will be added to this +ve or -ve
            possible_start = i
        curr_sum += list[i]

        if max_sum_subarray < curr_sum :
            max_sum_subarray = curr_sum
            # update left and right if new max_sum is achieved
            left  = possible_start
            right = i

    return left, right, max_sum_subarray


def maximum_sum_sub_array(list):
    max_sum = list[0]
    curr_sum = 0

    for num in list :
        if curr_sum < 0 :
            curr_sum = 0
        curr_sum += num

        if max_sum < curr_sum :
            max_sum = curr_sum

    return max_sum


if __name__ == "__main__" :
    testcase_1 = [-2, -3, -4]
    start, end, max_sum = maximum_sum_sub_array_with_indices(testcase_1)
    print(f"max sum of a subarray calculated {max_sum} - sub array: {testcase_1[start:end+1]}")

    testcase_2 = [2, 3, -8, 7, -1, 2, 3]
    max_sum = maximum_sum_sub_array(testcase_2)
    print(f"max sum of a subarray calculated {max_sum}")
