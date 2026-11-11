class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in numbers:
                if i > numbers.get(difference):
                    return[numbers.get(difference), i]
                else:
                    return [i,numbers.get(difference)]
                    
            if nums[i] not in numbers:
                numbers[nums[i]] = i 
     
