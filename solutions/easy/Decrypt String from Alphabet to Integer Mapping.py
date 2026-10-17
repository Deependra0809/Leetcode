// Title: Decrypt String from Alphabet to Integer Mapping
            // Difficulty: Easy
            // Language: Python
            // Link: https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

        for i in range(0, n):
        
        ans = ''
            if s[i] == '#':
                ans = ans[:-2]
                num = int(s[i-2] + s[i-1])
                ans += alphabet[num - 1]
            else:
                num = int(s[i])
                ans += alphabet[num - 1]
                
        return ans
