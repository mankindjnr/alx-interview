"""
write a function that takes an array of N integers that returns the smallest positive integer (>0) that
does not occur in the array given.

i.e given [1, 3, 6, 4, 1, 2]
    returns 5
    given [1, 2, 3]
    returns 4
    given[-1, -3]

assumption: N is an integer within the range: [1...100,000]
and each element of array is an integer within the range: [-1,000,000, 1,000,000]
"""
from typing import List


def solution(arr: List[int]) -> int:
    smallest_int: int
    
    """
    eliminate all negatives from the array and if the postive array left is empty, then the whole array
    was full of negatives and the smallest postive int can only be 1

        check if there are values between 0 and the minimum value of the postive array, if there are values, then the smallest
        possible integer can only be 1
    """
    positives = [item for item in arr if item > 0]
    print(positives)
    if len(positives) == 0 or min(positives) > 1:
        smallest_int = 1
        return smallest_int

    """
    if the whole array is uniform, then the smallest possible int is the one following the greatest value
    in the array
    """
    small_no: int = min(positives)
    large_no: int = max(positives)
 
    """extracting the missing values in the array if the array minimum is not greater than 1"""
    missing_values = [i for i in range(small_no, large_no) if i not in set(positives)]

    if len(missing_values) == 0:
        smallest_int = large_no + 1
        return smallest_int
    else:
        return (min(missing_values))


test_arr =  [0, 2, 4, 6, 8]
print(solution(test_arr))
