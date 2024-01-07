class Solution(object):
    def isAnagram(self, s, t):
        str1_list = list(s)
        str1_list.sort()
        str2_list = list(t)
        str2_list.sort()

        return (str1_list == str2_list)