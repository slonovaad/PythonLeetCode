from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, el in enumerate(nums):
            d[el].append(i)
        for key in d:
            for i in range(1, len(d[key])):
                if d[key][i] - d[key][i - 1] <= k:
                    return True
        return False
