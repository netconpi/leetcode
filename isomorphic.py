class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        swapped = {}

        for i in range(len(s)):
            if s[i] not in swapped.keys():
                swapped[s[i]] = t[i]
            else:
                if swapped[s[i]] != t[i]:
                    return False

        freq_s = {}
        freq_t = {}
        for i in range(len(s)):
            if s[i] not in freq_s.keys():
                freq_s[s[i]] = 1
            else:
                freq_s[s[i]] += 1
            if t[i] not in freq_t.keys():
                freq_t[t[i]] = 1
            else:
                freq_t[t[i]] += 1

        if [*freq_s.values()] == [*freq_t.values()]:
            return True
        else:
            return False 
