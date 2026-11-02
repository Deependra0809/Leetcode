// Title: Single Number
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/single-number/

        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        for i in range(0,l):
            if nums[i] not in num[:]:
        """
            num.remove(nums[i])
            num=nums[:]
                return nums[i]
