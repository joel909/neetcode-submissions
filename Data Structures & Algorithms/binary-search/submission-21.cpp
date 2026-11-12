class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        while (right>=left){
            int mid_point = (left+right)/2;
            if(nums[mid_point]>target){
                right = mid_point-1;
            }
            else if(nums[mid_point]<target){
                left = mid_point+1;
            }
            else{
                return mid_point;
            }
        }
        return -1;
    }
};
