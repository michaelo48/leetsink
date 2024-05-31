class Solution(object):
    def mergeAlternately(self, word1, word2):
        word1_len = len(word1)
        word2_len = len(word2)
        Common_Len = 0
        merged = ""

        if(word1_len> word2_len):
            Common_Len = word2_len
        else:
            Common_Len = word1_len

        for x in range(Common_Len):
            merged = merged + word1[x] + word2[x]
        if Common_Len == word1_len:
            return (merged+word2[Common_Len:])
        else:
            return merged + word1[Common_Len:]
     
        


        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        