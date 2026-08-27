class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s))
            out += "#"
            out += s
        return out

    def decode(self, s: str) -> List[str]:
        decoded = []
        while True:
            delim = s.find('#')
            if delim == -1:
                break
            length = int(s[:delim])
            word = s[delim + 1: delim + 1 + length]
            decoded.append(word)
            s = s[delim + 1 + length:]
        return decoded

