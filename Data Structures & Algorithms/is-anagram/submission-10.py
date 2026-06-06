class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early stop for string length mismatch
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t