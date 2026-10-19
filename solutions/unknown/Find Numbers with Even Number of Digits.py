// Title: Find Numbers with Even Number of Digits
            // Difficulty: Unknown
            // Language: Python
            // Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(0,len(nums)):
            if len(str(nums[i]))%2 == 0:
                c+=1
        return c
