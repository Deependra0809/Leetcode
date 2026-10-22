// Title: Alice and Bob Playing Flower Game
            // Difficulty: Medium
            // Language: Python
            // Link: https://leetcode.com/problems/alice-and-bob-playing-flower-game/

class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        count = 0
        modd = 0
        meven = 0
        if m%2 == 0:
