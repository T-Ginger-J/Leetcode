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
