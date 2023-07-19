from typing import List
import statistics


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def minMoves2(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
        Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
        In one move, you can increment or decrement an element of the array by 1.
        Test cases are designed so that the answer will fit in a 32-bit integer.
        '''  # noqa 501
        med = statistics.median(nums)
        if min(nums) == max(nums):
            return 0
        result = 0
        for i in nums:
            result += abs(i - med)
        return result

    def largestNumber(self, nums: List[int]) -> str:
        li_res = []
        for num in nums:
            for i in str(num):
                li_res += [int(i)]
        li_res.sort(reverse=True)
        result = ''
        for i in li_res:
            result += str(i)
        return result

    def reverseWords(self, s: str) -> str:
        '''
        https://leetcode.com/problems/reverse-words-in-a-string/submissions/
        Given an input string s, reverse the order of the words.
        A word is defined as a sequence of non-space characters.
        '''
        return ' '.join(s.split()[::-1])
