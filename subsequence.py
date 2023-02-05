class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # I'm too lazy to rewrite this...
        s, t = t, s
        
        len_alp = len(s)
        min_len = len(t)
        if min_len == 0:
            return True

        # iter busy
        itera = 0
        for i in range(len_alp):
            if s[i] == t[itera]:
                itera += 1
            
            if itera == min_len:
                return True
        
        return False