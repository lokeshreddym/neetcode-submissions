class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        groups = defaultdict(list)

        for i in nums:
            groups[i].append(i)
        ls=[]
        sorted_groups = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
        for i in range(k):
            ls.append(sorted_groups[i][0])
        return ls