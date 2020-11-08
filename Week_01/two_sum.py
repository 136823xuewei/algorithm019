class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        """
        docstring
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i