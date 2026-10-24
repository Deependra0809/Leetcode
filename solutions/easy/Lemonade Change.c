// Title: Lemonade Change
            // Difficulty: Easy
            // Language: C
            // Link: https://leetcode.com/problems/lemonade-change/

            {
            n10++;
            n5--;
            }else{
                return false;
            }
        }
        else
        {
            printf("%d %d",n5,n10);
            printf("\n");
            if(n10>=1 && n5>=1){
                n5--;
                n10--;
            }
            else if(n5>=3){
                n5-=3;
