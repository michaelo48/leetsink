class Solution:
    def minimumLength(self, s: str) -> int:
        start = 0
        end = len(s) - 1
        
        while start < end and s[start] == s[end]:
            char = s[start]
            
            while start <= end and s[start] == char:
                start += 1
            
  
            while start <= end and s[end] == char:
                end -= 1
        

        return max(0, end - start + 1)