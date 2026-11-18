class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int length = piles.size();
    int largest = 0;
    for(int i =0;i<length;i++){
        if(piles[i]>largest){
            largest = piles[i];
        }
    }
    int left = 1;
    int right = largest;
    int min_banana_per_hour;
    while (left<=right){
        int mid_point = (right+left)/2;
        long long total_hours_taken = 0;
        for(int i = 0;i<length;i++){
            long long hours_taken_per_pile = (((piles[i]-1)/mid_point) +1);
            // cout << "Hey " << "current hours is : "<< total_hours_taken << " currently adding  "<< (((piles[i]-1)/mid_point) +1) << " and Mid point is : "<< mid_point <<"\n"; 
            total_hours_taken = total_hours_taken + hours_taken_per_pile;
        }
        if (total_hours_taken<=h){
            min_banana_per_hour = mid_point;
            // cout << "min banan per hour was set to : " << min_banana_per_hour << " and it takes :  " << total_hours_taken  << "hours " << "\n";
            right = mid_point-1;
        }
        else if(total_hours_taken>h){
            left = mid_point+1;
        }

    }
    return min_banana_per_hour;
    }
};
