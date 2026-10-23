// Title: Climbing Stairs
            // Difficulty: Easy
            // Language: C
            // Link: https://leetcode.com/problems/climbing-stairs/

    
    int current = 0;
    int prev2 = 2; // ways to climb 2 stairs
    int prev1 = 1; // ways to climb 1 stair
    for (int i = 3; i <= n; i++) {
        current = prev1 + prev2;
        prev1 = prev2;
        prev2 = current;
    }
    
    return current;
}
