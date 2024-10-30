class Solution(object):
    def mergeAlternately(self, word1, word2):
        combo = ""  
        if len(word1) > len(word2):
            LoopLength = word2
            leftover = word1
        else:
            LoopLength = word1
            leftover = word2
        for x in range(0, len(LoopLength)):
            combo = combo + word1[x] + word2[x]
        if len(word1) != len(word2):
            combo = combo + leftover[-(len(leftover)-len(LoopLength)):]
        return combo


            
        