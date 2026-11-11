class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for number in range(len(nums)):

            possible = target -  nums[number]

            if possible in hash_map:
                return [hash_map[possible], number]
            
            hash_map[nums[number]] = number