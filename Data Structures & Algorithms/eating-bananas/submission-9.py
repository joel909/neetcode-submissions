
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #first find the median element i could use 
        right = piles[0]
        left = 1
        for pile in piles:
            if pile > right:
                right = pile
        k = 0
        while right>=left:
            total_sum = 0
            mid_point = (right+left)//2
            for pile in piles:
                total_sum += math.ceil(pile/mid_point)
            if total_sum>h:
                left = mid_point+1
            elif total_sum<=h:
                right = mid_point-1
                k  = mid_point
        return (k)