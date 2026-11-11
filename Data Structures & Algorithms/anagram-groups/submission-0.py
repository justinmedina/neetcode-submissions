class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            count = {}

            for letter in word:
                if letter not in count:
                    count[letter] = 1
                else:
                    count[letter] += 1
            
            key = tuple(sorted(count.items()))

            if key not in anagram:
                anagram[key] = []
            
            anagram[key].append(word)
        
        return list(anagram.values())


