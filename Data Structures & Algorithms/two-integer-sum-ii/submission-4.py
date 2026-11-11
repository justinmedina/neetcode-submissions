class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        h = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in h: 
                if h.get(diff) > i:
                    return [i+1, h.get(diff)+1]
                else:
                    return [h.get(diff)+1, i+1]
            else:
                h[numbers[i]] = i
