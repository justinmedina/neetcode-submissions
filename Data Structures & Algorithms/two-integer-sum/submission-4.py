class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for number in range(len(nums)):
            hash_map[nums[number]] = number 
            for j in range(number+1,len(nums)):
                cor_num = target - nums[j]
                if cor_num in hash_map:
                    return [number,j]