// Title: Minimum Value of Merged Integers
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/minimum-value-of-merged-integers/

        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(0,n,2):
            if int(str(nums[i])+str(nums[i+1])) <=min:
        min=int(str(nums[0])+str(nums[1]))
                min= int(str(nums[i])+str(nums[i+1]))
        return min
        
