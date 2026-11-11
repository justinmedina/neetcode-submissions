class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams={} # dictionary of list of anagrams
        """
        (a,1) , (c,1) , (t,1) : [act, cat]
        """

        for word in strs:
            count={}
            """
            c:1
            a:1
            t:1
            """
            for letter in word:
                if letter not in count:
                    count[letter] = 1
                else:
                    count[letter] += 1

            key = tuple(sorted(count.items()))
 
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

        return list(anagrams.values())



