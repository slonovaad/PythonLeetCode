from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        ans = []
        for key in d1:
            if key in d2:
                ans += [key] * min(d1[key], d2[key])
        return ans
