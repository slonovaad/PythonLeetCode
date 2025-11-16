from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = dict()
        for el in strs:
            counters[el] = Counter(el)
        strs.sort(key=lambda x: (len(x), sorted(counters[x].items())))
        ans = [[strs[0]]]
        for el in strs[1:]:
            if counters[ans[-1][-1]] == counters[el]:
                ans[-1].append(el)
            else:
                ans.append([el])
        return ans
