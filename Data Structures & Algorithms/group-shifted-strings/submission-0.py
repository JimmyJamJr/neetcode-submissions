class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def get_key(s):
            shift = ord(s[0])
            return "".join(chr((ord(c) - shift) % 26 + ord('a')) for c in s)

        
        mapping = {}
        
        for i, s in enumerate(strings):
            key = get_key(s)
            mapping[key] = mapping.get(key, []) + [s]
        
        return list(mapping.values())

