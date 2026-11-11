class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for number in range(len(nums)):
            if nums[number] in hash_map:
                return True
            else:
                hash_map[nums[number]] = number
        return False 
