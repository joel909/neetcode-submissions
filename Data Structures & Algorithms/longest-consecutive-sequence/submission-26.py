class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        # print("this is the set : ",nums)
        for i in set(nums):
            count = 0
            # print("checking for :",i)
            for k in range(0,len(set(nums))):
                # print("checking if is there",i+k)
                if (i+k in set(nums)):
                    # print("match")
                    count +=1
                else:
                    print("------Break------")
                    break

            if (count>max_len):
                max_len = count
                        # count = 0r
            # print('-----------')            
            # print("count is",count)
            # print('-----------')
                    
        return max_len



        