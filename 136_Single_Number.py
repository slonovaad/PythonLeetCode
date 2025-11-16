class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set(nums)
        return -1 * (sum(nums) - 2 * sum(unique))
