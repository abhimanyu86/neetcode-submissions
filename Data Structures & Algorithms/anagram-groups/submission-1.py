from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))   # e.g. "eat" -> ('a','e','t')
            groups[key].append(s)
        return list(groups.values())