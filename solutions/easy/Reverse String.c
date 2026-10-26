// Title: Reverse String
            // Difficulty: Easy
            // Language: C
            // Link: https://leetcode.com/problems/reverse-string/

void reverseString(char* s, int sSize) {
    for(int i=1;i<=sSize/2;i++){
        char temp=s[sSize-i];
    }
        s[sSize-i]=s[i-1];
        s[i-1]=temp;
    return ;
}
