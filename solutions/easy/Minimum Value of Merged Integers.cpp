// Title: Minimum Value of Merged Integers
            // Difficulty: Easy
            // Language: C++
            // Link: https://leetcode.com/problems/minimum-value-of-merged-integers/

public:
    int minMergedInteger(vector<int>& nums) {
        int n=nums.size();
        int min=stoi(to_string(nums[0])+to_string(nums[1]));
            if (stoi(to_string(nums[i])+to_string(nums[i+1])) <=min)
                min= stoi(to_string(nums[i])+to_string(nums[i+1]));
        return min;
        }
class Solution {
        for(int i=0;i<n;i=i+2){
    }
