from typing import List, Optional
from medium import ListNode


class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        https://leetcode.com/problems/counting-bits/description/
        Given an integer n, return an array ans of length n + 1
        such that for each i (0 <= i <= n), ans[i] is the number
        of 1's in the binary representation of i.
        '''
        result = []
        for i in range(n + 1):
            result += [0]
            while i > 0:
                if i % 2:
                    result[-1] += 1
                i //= 2
        return result

    def longestPalindrome(self, s: str) -> int:
        length = len(s)
        max = 0
        for i in range(length):
            for j in range(i, length):
                substr = s[i:j]
                if substr == substr[::-1]:
                    now = len(substr)
                    if now > max:
                        max = now
        return max

    def checkPerfectNumber(self, num: int) -> bool:
        '''
        https://leetcode.com/problems/perfect-number/
        A perfect number is a positive integer that
        is equal to the sum of its positive divisors,
        excluding the number itself. A divisor of an
        integer x is an integer that can divide x evenly.
        Given an integer n, return true if n is a perfect
        number, otherwise return false.
        '''
        result = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                result += i
                print(i)
        return num == result

    def lengthOfLastWord(self, s: str) -> int:
        '''
        https://leetcode.com/problems/length-of-last-word/description/
        Given a string s consisting of words and spaces,
        return the length of the last word in the string.
        '''
        return len(s.split()[-1])

    def singleNumber(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/single-number/description/
        Given a non-empty array of integers nums, every element
        appears twice except for one. Find that single one.
        '''
        r = 0
        for i in nums:
            r = i ^ r
        return r

    def isAnagram(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/valid-anagram/description/
        Given two strings s and t, return true if t
        is an anagram of s, and false otherwise.
        '''
        if len(t) != len(s):
            return False
        return sorted(s) == sorted(t)

    def addBinary(self, a: str, b: str) -> str:
        '''
        https://leetcode.com/problems/add-binary/description/
        Given two binary strings a and b,
        return their sum as a binary string.
        '''
        # extra = 0
        # result = ''
        # len_a = len(a)
        # len_b = len(b)
        # if len_a != len_b:
        #     longest = len(max(a, b, key=len))
        #     if len_a < longest:
        #         a = '0' * (longest - len_a) + a
        #     elif len_b < longest:
        #         b = '0' * (longest - len_b) + b
        # for i, j in zip(a[::-1], b[::-1]):
        #     num = int(i) + int(j) + extra
        #     if num > 1:
        #         result += str(num - 2)
        #         extra = 1
        #         continue
        #     result += str(num)
        #     extra = 0
        # while extra:
        #     result += '1'
        #     extra -= 1
        # return result[::-1]
        return bin(int(a, 2) + int(b, 2))[2:]

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        https://leetcode.com/problems/greatest-common-divisor-of-strings/
        For two strings s and t, we say "t divides s" if and
        only if s = t + ... + t (i.e., t is concatenated with
        itself one or more times).
        '''
        # longest = max(str1, str2, key=len)
        # long = ''
        # for i in range(len(longest)):
        #     for j in range(len(longest)):
        #         str1_r = str1.replace(longest[i:j], '')
        #         str2_r = str2.replace(longest[i:j], '')
        #         if not str1_r and not str2_r:
        #             if len(long) < len(longest[i:j]):
        #                 long = longest[i:j]
        # return long
        # if str1.replace(str2, '') == '':
        #     return str2
        shortest = min(str1, str2, key=len)
        longest = max(str1, str2, key=len)
        if not longest.replace(shortest, ''):
            return shortest
        for i in range(len(shortest), 0, -1):
            if not shortest.replace(str1[i:], ''):
                if longest.replace(str1[i:], ''):
                    continue
                else:
                    return longest[i:]
        return ''

    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        https://leetcode.com/problems/merge-strings-alternately/description/
        You are given two strings word1 and word2. Merge the strings by adding
        letters in alternating order, starting with word1. If a string is
        longer than the other, append the additional letters onto the end of
        the merged string.
        '''
        longest = len(max(word1, word2, key=len))
        result = ''
        for i in range(longest):
            result += word1[i:i + 1] + word2[i:i + 1]
        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/middle-of-the-linked-list/description/
        Given the head of a singly linked list, return the list node from the
        middle.
        '''
        nodes = []
        while head:
            nodes += [head.val]
            head = head.next
        length = len(nodes)
        if length % 2 != 0:
            nodes = nodes[length // 2 + 1:]
        else:
            nodes = nodes[length // 2:]
        new_head = ListNode(nodes.pop(0))
        head = new_head
        while nodes:
            new_head.next = ListNode(nodes.pop(0))
            new_head = new_head.next
        return head

    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        '''
        https://leetcode.com/problems/minimum-distance-to-the-target-element/description/
        Given an integer array nums (0-indexed) and two integers target and start, find
        an index i such that nums[i] == target and abs(i - start) is minimized. Notethat abs(x) is the absolute value of x.
        or like this
        return min([abs(i - start) for i in range(len(nums)) if nums[i] == target])
        ''' # noqa 501
        for i in range(len(nums)):
            if target in nums[abs(start - i): start + i + 1]:
                return i

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        https://leetcode.com/problems/ransom-note/description/
        Given two strings ransomNote and magazine, return true
        if ransomNote can be constructed by using the letters
        from magazine and false otherwise.
        '''
        for i in ransomNote:
            if i not in magazine:
                return False
            ransomNote = ransomNote[1:]
            magazine = magazine[:magazine.index(i)] + magazine[magazine.index(i) + 1:]  # noqa 501
        return True

    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/is-subsequence/description/
        Given two strings s and t, return true if s is a
        subsequence of t, or false otherwise.
        '''
        for i in range(len(s)):
            if s[i] not in t:
                return False
            t = t[t.index(s[i]) + 1:]
        return True

    def maxProfit(self, prices: List[int]) -> int:
        if sorted(prices, reverse=True) == prices:
            return 0
        glob_max = 0
        for i in range(len(prices) - 1):
            loc_max = max([j - prices[i] for j in prices[i+1:][::-1]])
            if loc_max > glob_max:
                glob_max = loc_max
        return glob_max

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # noqa 501
        '''
        https://leetcode.com/problems/merge-two-sorted-lists/description/
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list. The list should be made by
        splicing together the nodes of the first two lists.
        '''
        loc = ListNode()
        result = loc
        var = []
        while list1 or list2:
            if list1:
                var += [list1.val]
                list1 = list1.next
            if list2:
                var += [list2.val]
                list2 = list2.next
        for i in sorted(var):
            print(i)
            loc.next = ListNode(i)
            loc = loc.next

        return result
