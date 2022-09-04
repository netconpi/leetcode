
# Link: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ann_dict = {}
        output_dict = []
        if len(strs) == 1:
            return [strs]
        for i in strs:
            alph = ''.join(sorted(i))
            try:
                ann_dict[alph].append(i)
            except KeyError:
                ann_dict[alph] = [i]

        for v in ann_dict.values():
            output_dict.append(v)

        return output_dict