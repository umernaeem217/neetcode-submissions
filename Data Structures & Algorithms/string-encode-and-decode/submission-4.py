class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = 0
        res = []
        while l < len(s):
            j = l
            count = []
            while j < len(s) and s[j] != '#':
                count.append(s[j])
                j+=1
            length = int("".join(count[:j]))
            res.append(s[j+1: j+length+1])
            l = j+length+1
        return res



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))