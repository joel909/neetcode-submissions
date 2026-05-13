class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        max_length = 0
        if (len(a)==0):
            length = 0
        else:
            length = 1
        for item in a:
            if item+1 in a:
                length += 1
            else:
                if max_length<length:
                    max_length = length
                length =1
        return max_length


        