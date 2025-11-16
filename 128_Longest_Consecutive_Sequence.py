class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 1:
            return len(nums)
        ans = 1
        s = 0
        f = 1
        nums.sort()
        while f < len(nums):
            if nums[f] - nums[f - 1] != 1:
                ans = max(ans, f - s)
                s = f
            f += 1
        if s == 0 and f == len(nums):
            return len(nums)
        if nums[-1] - nums[-2] == 1:
            ans = max(ans, f - s)
        return ans
