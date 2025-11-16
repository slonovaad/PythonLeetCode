from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [el[0] for el in counter_items[:k]]
