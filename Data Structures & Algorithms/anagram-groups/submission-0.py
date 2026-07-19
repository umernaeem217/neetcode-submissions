class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sorted_word = str(sorted(word))
            dic[sorted_word].append(word)
        
        res = []
        for key in dic.keys():
            res.append(dic[key])
        return res
                


