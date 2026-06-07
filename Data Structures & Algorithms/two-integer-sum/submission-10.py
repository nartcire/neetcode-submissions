class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary where the key is the second input and
        # the value is the index of the first input
        matching_dict = {}
        
        for i, num in enumerate(nums):
            if num in matching_dict:
                return [matching_dict[num], i]

            matching_dict[target - num] = i

        