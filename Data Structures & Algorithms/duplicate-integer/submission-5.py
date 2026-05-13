class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        old_el = []
        for i in nums:
            if i in old_el:
                return True
            old_el.append(i)
        return False
        