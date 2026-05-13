class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = (sorted(set(nums)))
        if (len(a)==0):
            max_length = 0
        else:
            max_length = 1
        length = 1
        for i in range(0,len(a)-1):
            if a[i]-a[i+1]==-1:
                length += 1
                print(length)
                if length>max_length:
                    max_length = length
            else:
                print(length)
                length = 1
                
        return max_length


        