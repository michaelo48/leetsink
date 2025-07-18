class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) == 0:
            return True
        for x in t:
            if s[i] == x:
                i += 1
            if i > len(s) - 1 :
                return True
        return False
