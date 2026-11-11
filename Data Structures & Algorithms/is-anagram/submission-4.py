class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #one dictionary, when we add we do a cehck for both list and then add and subtract

        anagram ={}

        if len(s) != len(t):
            return False
        
        for letter in range(len(s)):
            if s[letter] in anagram:
                anagram[s[letter]] += 1
            else:
                anagram[s[letter]] = 1
            if t[letter] in anagram:
                anagram[t[letter]] -= 1
            else:
                anagram[t[letter]] = -1 

        for value in anagram.values():
            if value != 0:
                return False
        return True 