class Solution:

    def encode(self, strs: List[str]) -> str:
        n = ""
        for s in strs:
            n = n + s + "😀"
        return n

    def decode(self, s: str) -> List[str]:
        l = []
        c = ""
        for x in s:
            if(x != "😀"):
                c = c + x
            else:
                l.append(c)
                c = ""
        return l