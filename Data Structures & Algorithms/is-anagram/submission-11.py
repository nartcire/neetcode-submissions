class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early stop for string length mismatch
        if len(s) != len(t):
            return False

        anagram_dict = {}

        for c in s:
            anagram_dict[c] = anagram_dict.get(c, 0) + 1

        for c in t:
            if c not in anagram_dict:
                return False

            anagram_dict[c] -= 1

        for value in anagram_dict.values():
            if value != 0:
                return False

        return True