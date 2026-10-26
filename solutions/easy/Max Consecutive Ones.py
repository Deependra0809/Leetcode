// Title: Max Consecutive Ones
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/max-consecutive-ones/

        n=len(nums)
        c=0
        for i in range(0,n):
        maxc=0
            if nums[i]==1:
                c+=1
                if(c>=maxc):
                    maxc=c
            else:
                c=0
        return maxc

