from typing import List, Optional
import statistics


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return self.val


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

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        https://leetcode.com/problems/rotate-image/description/
        Do not return anything, modify matrix in-place instead.
        You are given an n x n 2D matrix representing an image,
        rotate the image by 90 degrees (clockwise).
        """
        matrix[:] = matrix[::-1]
        len_str = len(matrix[0])
        result = []
        for i in range(len_str):
            result.append([])
            for j in range(len_str):
                print(result[i])
                result[i] += [matrix[j][i]]
        return result

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/swap-nodes-in-pairs/description/
        Given a linked list, swap every two adjacent nodes and return its head.
        '''
        try:
            node = head
            next_node = head.next
            while node and next_node:
                node.val, next_node.val = next_node.val, node.val
                node = node.next.next
                next_node = next_node.next.next
            return head
        except AttributeError:
            return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # noqa 501
        """
        https://leetcode.com/problems/add-two-numbers/description/
        You are given two non-empty linked lists representing two non-negative
        integers. The digits are stored in reverse order, and each of their
        nodes contains a single digit. Add the two numbers and return the sum
        as a linked list.
        """
        extra = 0
        result = ListNode()
        temp = result
        while l1 or l2:
            temp.next = ListNode()
            sum_nodes = 0
            if l1:
                sum_nodes += l1.val
                l1 = l1.next
            if l2:
                sum_nodes += l2.val
                l2 = l2.next
            sum_nodes += extra
            extra = 0
            if sum_nodes > 9:
                extra, sum_nodes = divmod(sum_nodes, 10)
            temp.next.val = sum_nodes
            temp = temp.next
        if extra:
            temp.next = ListNode(extra)
        return result.next

    def myAtoi(self, s: str) -> int:
        'converts string to int'
        s = s.strip()
        result = ''
        minus = False
        for i in range(len(s)):
            if s[i] == '-':
                minus = True
            if s[i].isdigit():
                for j in s[i:]:
                    if j.isdigit():
                        result += j
                else:
                    return int(result) if not minus else int('-' + result)
            elif s[i].isalpha():
                return None

    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                now = (j - i) * height[j]
                if now > max:
                    print(j-i, height[j])
                    max = now
        return max

a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))