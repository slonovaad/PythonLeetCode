from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, el in enumerate(s):
            if counts[el] == 1:
                return i
        return -1
