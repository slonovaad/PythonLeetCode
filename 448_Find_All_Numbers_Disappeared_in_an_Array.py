class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = dict()
        for i in range(1, len(nums) + 1):
            d[i] = 0
        for el in nums:
            d[el] = 1
        return [i for i in range(1, len(nums) + 1) if not d[i]]
