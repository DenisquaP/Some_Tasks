from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array to the
        right by k steps, where k is non-negative.
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            for _ in range(k):
                nums[:] = [nums.pop()] + nums
        else:
            nums[:] = nums[-k:] + nums[:-k]
