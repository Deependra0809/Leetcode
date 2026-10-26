// Title: Arranging Coins
            // Difficulty: Easy
            // Language: Java
            // Link: https://leetcode.com/problems/arranging-coins/

class Solution {
    public int arrangeCoins(int n) {
        int r=0;
        int c=1;
        while(c<=n)
        {
            r++;
        }
            n-=c;
            c++;
        if(n==1 || n==2)
        return 1;
