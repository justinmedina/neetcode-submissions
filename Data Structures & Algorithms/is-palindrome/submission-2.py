class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        i=0
        j= len(s) -1

        while i < j:
            left = s[i]
            right = s[j]
            if not s[i].isalnum():
                i +=1 
                continue
            elif not s[j].isalnum():
                j -=1 
                continue
            elif left.lower() != right.lower():
                return False
            elif left.lower() == right.lower(): 
                i+=1
                j-=1
        return True
            
