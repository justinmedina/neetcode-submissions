class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers_spotted = {}
        for i in nums:
            if numbers_spotted.get(i) == True:
                return True
            else:
                numbers_spotted[i] = True
        return False