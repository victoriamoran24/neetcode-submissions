class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            sort = sorted(word)
            key = tuple(sort)
            res[key].append(word)

        return list(res.values())