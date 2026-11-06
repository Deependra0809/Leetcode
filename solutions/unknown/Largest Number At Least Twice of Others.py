// Title: Largest Number At Least Twice of Others
            // Difficulty: Unknown
            // Language: Python
            // Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        lt=max(nums)
        lti=nums.index(lt)
        for i in range(0,n):
            if lt<nums[i]*2 and lt!=nums[i]:
