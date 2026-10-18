// Title: Number of Steps to Reduce a Number to Zero
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

        :rtype: int
        """
        c=0
        while num!=0:
            if num%2==0:
                num=num/2
            else:
                num=num-1
                c=c+1
                c=c+1
        return c
