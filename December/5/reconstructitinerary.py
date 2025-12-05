# LeetCode 332: Reconstruct Itinerary
# Explanation:
# We must use all tickets exactly once and build the lexicographically smallest itinerary.
# This is an Eulerian path problem in a directed graph.
#
# Approach (Hierholzer’s Algorithm):
# 1. Build adjacency list: graph[src] = min-heap of destinations.
# 2. Always choose smallest lexical destination first → use heapq.
# 3. DFS until you cannot go deeper; then add airport to route.
# 4. Reverse the result at the end.
#
# Time Complexity: O(E log E)
# Space Complexity: O(E)

from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            while graph[airport]:
                nxt = heapq.heappop(graph[airport])
                dfs(nxt)
            route.append(airport)

        dfs("JFK")
        return route[::-1]
