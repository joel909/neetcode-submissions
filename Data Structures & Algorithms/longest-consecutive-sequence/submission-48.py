class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        li = set(nums)
        print(li)
        starting_points = []
        for i in li:
            if i-1 not in li and i+1 in li :
                starting_points.append(i)
        print(starting_points)
        if len(li) == 0:
            max_count = 0
        else:
            max_count =1
        for i in starting_points:
            count = 1
            for k in range(1,len(li)):
                if (i+k) in li:
                    count +=1 
                else:
                    break
            if count>max_count:
                max_count=count
        return(max_count)
        