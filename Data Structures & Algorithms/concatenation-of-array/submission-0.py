class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # We take nums and concatenat it to the end of the of the list
        ans = nums + nums

        return ans