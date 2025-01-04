# Given a sorted array, find two numbers that add up to a given total.

class TwoSumSortedArray :

    @staticmethod
    def find_the_pair(arr, sum):
        left, right  = 0, len(arr) - 1

        while left < right :
            calculated_sum = arr[left] + arr[right]
            if calculated_sum == sum :
                return arr[left], arr[right]
                # if all possible pairs are required we store this pair in an array and move on instead of returning
            elif calculated_sum < sum :
                left += 1
            else :
                right -= 1

        return -1

if __name__ == "__main__" :
    list = [-30, -12, -2, -1, 0, 2, 3,5,7,9,10,23,56]
    required_sum = 2

    output = TwoSumSortedArray.find_the_pair(list, required_sum)
    if output == -1 :
        print(f"there are no pairs where sum is {required_sum}")
        exit()
    print(f"Required sum can be achieved with {output}")