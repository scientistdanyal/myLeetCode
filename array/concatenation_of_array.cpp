class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {

        int n = nums.size();
        int m = n * 2;

        vector<int> arr(m);
     
        for ( int i = 0; i < n; i++){
            arr[i] = nums[i];
            arr[i+n] = arr[i];
        }
        return arr;
    }
};