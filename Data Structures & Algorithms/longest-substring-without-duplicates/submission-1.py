class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexA = 0
        indexB = 0
        largest_len = 0
        item_index_map = {}
        for index,item in enumerate(s):
            if item in item_index_map:
                if len(item_index_map)>largest_len:
                    largest_len = len(item_index_map)

                old_item_index = item_index_map[item]
                for i in range(indexB,old_item_index+1):
                    item_index_map.pop(s[i])
                indexB = old_item_index+1
                item_index_map[item] = index
            else:
                indexA+=1
                item_index_map[item] = index
                if (index+1==len(s)):
                    if len(item_index_map)>largest_len:
                        largest_len = len(item_index_map)
            
        # return len(item_index_map) 
        return (largest_len)
        # print(item_index_map,indexA,indexB)
        