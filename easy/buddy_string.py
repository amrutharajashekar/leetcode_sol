class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        target = 0
        if len(s) != len(goal):
            return False
        swap = ''
        goal1 = ''
        
        d = dict()
        same_alpha = False
        for i in range(len(s)):
            
            if s[i] in d:
                d[s[i]] += 1
                same_alpha = True
            else:
                print(s[i])
                d[s[i]] = 1
                
            if s[i] != goal[i]:
                target += 1
                swap += s[i]
                goal1= goal[i] + goal1
            
            if target > 2:
                return False
            
        print(swap, goal1,target,same_alpha,d)
        print((swap != '' and swap == goal1) or (target == 0 and same_alpha))
        if (swap != '' and swap == goal1) or (target == 0 and same_alpha):
            return True
        if target < 2:
            return False
        
        return False
