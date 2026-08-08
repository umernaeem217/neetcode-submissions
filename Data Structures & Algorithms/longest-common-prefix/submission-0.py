class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0 
        res = []
        while True:
            character = ''
            for s in strs:
                if i >= len(s):
                    return "".join(res)
                if character and s[i] != character:
                    return "".join(res)
                character = s[i]
            i+=1
            res.append(character)
        return "".join(character)