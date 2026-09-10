import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)              # (1)
        for u, v, w in times:                   # (2)
            edges[u].append((v, w))

        minHeap = [(0, k)]                      # (3)
        visit = set()                            # (4)
        t = 0                                     # (5)

        while minHeap:                            # (6)
            w1, n1 = heapq.heappop(minHeap)        # (7)
            if n1 in visit:                         # (8)
                continue

            visit.add(n1)                           # (9)
            t = w1                                   # (10)

            for n2, w2 in edges[n1]:                  # (11)
                if n2 not in visit:                    # (12)
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1              # (13)