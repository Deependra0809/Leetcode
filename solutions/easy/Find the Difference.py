// Title: Find the Difference
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
           val=0
           lt=len(t)
           ls=len(s)
           for i in range(0,lt):
               val=val+ord(t[i])
           for j in range(0,ls):
              val=val-ord(s[j])
           return chr(val)
    
