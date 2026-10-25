// Title: Lemonade Change
            // Difficulty: Easy
            // Language: C++
            // Link: https://leetcode.com/problems/lemonade-change/

                } else {
                    return false;
                }
            }
            else {
                if(n10 >= 1 && n5 >= 1) {
                    n10--;
                    n5--;
                }
                else if(n5 >= 3) {
                    n5 -= 3;
                }
