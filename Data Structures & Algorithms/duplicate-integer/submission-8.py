class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # We can just use a set here -- i'll write up a more algorithmic
        # solution though for practice

        num_set = set(nums)

        return len(num_set) != len(nums)