// Title: Find the Difference
            // Difficulty: Easy
            // Language: C
            // Link: https://leetcode.com/problems/find-the-difference/

    c=0;
    while(s[c]!='\0')
    {
        sum-=s[c];
    }
        c++;
    while(t[c]!='\0')
    {
        sum+=t[c];
char findTheDifference(char* s, char* t) {
    int sum=0,c=0;
