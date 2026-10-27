// Title: Arranging Coins
            // Difficulty: Easy
            // Language: C
            // Link: https://leetcode.com/problems/arranging-coins/

        while(c<=n)
        {
            r++;
            n-=c;
            c++;
        }
int arrangeCoins(int n) {
      if(n==1 || n==2)
        return 1;
        int r=0;
        int c=1;
