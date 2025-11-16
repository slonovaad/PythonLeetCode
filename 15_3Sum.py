from collections import defaultdict, Counter


class Solution:
    def find_2sum(self, nums: List[int], k: int, counter: Dict[int, int]) -> List[int]:
        ans = []
        for el in nums:
            if k - el in counter:
                ans.append([el, k - el])
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        nums = sorted(list(set(nums)))
        ans = []
        used = defaultdict(set)
        for i, el in enumerate(nums):
            two_sum = self.find_2sum(nums[i:], -el, counter)
            if len(two_sum) > 0:
                for sm_2 in two_sum:
                    ans_el = [el, sm_2[0], sm_2[1]]
                    if (sm_2[0] not in used[el] and
                            ans_el.count(el) <= counter[el] and
                            ans_el.count(sm_2[0]) <= counter[sm_2[0]] and
                            ans_el.count(sm_2[1]) <= counter[sm_2[1]]
                    ):
                        ans.append(ans_el)
                    used[el].add(sm_2[0])
                    used[el].add(sm_2[1])
                    used[sm_2[0]].add(el)
                    used[sm_2[0]].add(sm_2[1])
                    used[sm_2[1]].add(el)
                    used[sm_2[1]].add(sm_2[0])
        return ans
