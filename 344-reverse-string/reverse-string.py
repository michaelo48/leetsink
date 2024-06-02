class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        