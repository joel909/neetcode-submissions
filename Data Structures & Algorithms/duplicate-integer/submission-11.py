class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for item in nums:
            value = table.get(item)
            if value is None:
                table[item] = 1
            else :
                return True
        return False
        