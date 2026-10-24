// Title: Max Consecutive Ones
            // Difficulty: Easy
            // Language: C
            // Link: https://leetcode.com/problems/max-consecutive-ones/

        } else {
            c = 0;
        }

        if (c > maxc) {
            maxc = c;
        }
    }

    return maxc;
}
