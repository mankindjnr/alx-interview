"""
Given an array of integers "nums" and an integer "target", return indices of the two 
numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order.
"""
from typing import List
import time

start_time = time.time()
def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for idx in range(length):
        for index, item in enumerate(nums):
            if idx != index:
                if nums[idx] + item == target:
                    return (idx, index)

lst = [1, 2, 3, 4, 5]
target = 7
print(twoSum(lst, target))

def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    for idx in range(length):
        left = target - nums[idx]
        lst = nums.pop(idx)
        if left in lst:
            

print(twoSum2(lst, target))
