from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = Counter(s)
        counts_t = Counter(t)
        return counts_s == counts_t
