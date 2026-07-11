class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        # Count frequency of each character in magazine
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        # Check if ransomNote can be constructed
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            count[ch] -= 1

        return True