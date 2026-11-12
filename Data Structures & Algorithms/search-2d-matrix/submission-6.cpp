class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
       int left,right,mid_point,point_value,total_size,rows,cols;
        left = 0;
        rows = matrix.size();
        cols = matrix[0].size();
        total_size = rows*cols;
        right = (total_size)-1;
        while(right>=left){
            mid_point = (left+right)/2;
            point_value = matrix[mid_point/cols][mid_point-((mid_point/cols)*cols)];
            if(point_value>target){
                right = mid_point-1;
            }
            else if(point_value<target){
                left = mid_point+1;
            }
            else{
                return true;
            }
        }
        return false; 
    }
};
