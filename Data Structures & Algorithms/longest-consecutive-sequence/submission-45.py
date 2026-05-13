class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        li = sorted(set(nums))
        print(li)
        count = 1
        max_count = 0
        for i in range(0,len(li)):
            if li[i]-1 in li:
                count += 1
            else:
                if max_count<count:
                    max_count = count
                count = 1
            if max_count<count:
                max_count = count
        return max_count
            



        