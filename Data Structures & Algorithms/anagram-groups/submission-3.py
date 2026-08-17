from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            counter = [0] * 26
            for i in range(len(word)):
                counter[ord(word[i]) - ord('a')]+=1
            dic[tuple(counter)].append(word)
        return list(dic.values())