class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 1:
        #     return strs[0]
        # res = strs[0]
        # for i in range(1, len(strs)):
        #     j = 0
        #     while j < min(len(res), len(strs[i])):
        #         if res[j] != strs[i][j]:
        #             break
        #         j+=1
        #     res = res[:j]
        # return res
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]