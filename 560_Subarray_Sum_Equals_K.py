from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = [0] * len(nums)
        prefixes[0] = nums[0]
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] + nums[i]
        ans = 0
        count_d = defaultdict(int)
        for f in range(len(prefixes)):
            ans += count_d[prefixes[f] - k]
            count_d[prefixes[f]] += 1
            if prefixes[f] == k:
                ans += 1
        return an
