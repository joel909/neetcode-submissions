class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        indexes = []

        for i in range(len(nums)):
            if maps.get(target - nums[i]) is None:
                maps[target - nums[i]] = i
            else:
                if nums[i]*2 == target:
                    indexes.append(maps[target - nums[i]])
                    indexes.append(i)
                    return indexes
        print(maps)
        for i in range(len(nums)):
            if nums[i] in maps and maps[nums[i]] != i:
                indexes.append(i)

        return indexes

        