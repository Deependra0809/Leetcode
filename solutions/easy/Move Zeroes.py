// Title: Move Zeroes
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/move-zeroes/

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        for i in range(0,l):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)

