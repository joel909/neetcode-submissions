class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_frequent = []
        total_map = {}

        for item in nums:
            if total_map.get(item) == None:
                total_map[item] = 1
            else:
                total_map[item] += 1
        for required_frequency in range(0, k):
            highest_frequency_no = nums[0]
            for key in total_map:
                # print(f"key: {key}, total_map[key]: {total_map[key]}, highest_frequency_no: {highest_frequency_no}")
                if total_map[key] > total_map[highest_frequency_no]:
                    highest_frequency_no = key
                    # print(f"highest_frequency_no: {highest_frequency_no}")

            k_frequent.append(highest_frequency_no)
            total_map[highest_frequency_no] = 0

        return k_frequent
        