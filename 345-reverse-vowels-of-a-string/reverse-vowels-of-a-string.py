class Solution(object):
    def reverseVowels(self, s):
        vowel = 'AaEeUuIiOo'
        start = 0
        s = list(s)
        end = len(s)-1
        
        
        while start < end:
            if(s[start] not in vowel):
                
                start += 1
                continue
            if(s[end] not in vowel):
                
                end -= 1
                continue
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1    
        newWord = ''.join(s) 
        return newWord     
        """
        :type s: str
        :rtype: str
        """
        