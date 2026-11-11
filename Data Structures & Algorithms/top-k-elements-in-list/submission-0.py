class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[]for _ in range(len(nums)+1)]
        return_list=[]
        i = 1
        for number in nums:
            if number in freq:
                freq[number] += 1
            else:
                freq[number] = 1
        for pair in freq.items():
            num = pair[0]
            count = pair[1]
            buckets[count].append(num)
        for i in range(len(buckets)-1,-1,-1):
            if len(buckets[i]) > 0:
                for num in buckets[i]:
                    return_list.append(num)
                    if len(return_list) >= k:
                        return return_list

            