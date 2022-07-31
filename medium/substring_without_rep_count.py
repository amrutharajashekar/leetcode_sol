class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max = 0
        i = 0
        len_s = len(s)
        count = 0
        left_ptr= 0

        d = dict()
        while i < len_s : 
            repeat = False
            
            while not(repeat) and i < len_s:
                if s[i] not in d   : 
                    count += 1
                    i += 1
                elif s[i] in d and  d[s[i]] < left_ptr : 
                    count += 1
                    i += 1
                else:
                    
                    if max < count : 
                        max = count 
                        
                    left_ptr = d[s[i]] + 1
                    count = i - d[s[i]] 
                    repeat = True
                    
                    i+= 1

                d[s[i-1]] = i -1

                    
            
            print(s[i-1], count)
        if max < count : 
            max = count 
        return max 
