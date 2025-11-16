class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sm = sum(nums)
        n = len(nums)
        progression_sm = n * (n + 1) // 2
        return progression_sm - nums_sm
i