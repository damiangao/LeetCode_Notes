class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)

        # build station_route_map
        station_route_map = collections.defaultdict(list)
        for i in range(n):
            for state in routes[i]:
                station_route_map[state].append(i)

        # build undirected graph
        adj_list = collections.defaultdict(set)
        for i in range(n):
            for state in routes[i]:
                adj_list[i].update(station_route_map[state])
        
        # BFS
        res = n + 1
        for start_route in station_route_map[source]:
            visted = [0] * n
            curr_trip = 0
            q = collections.deque([start_route])
            visted[start_route] = 1
            while q:
                curr_trip += 1
                for _ in range(len(q)):
                    curr_route = q.popleft()
                    if target in routes[curr_route]:
                        res = min(res, curr_trip)
                        break
                    for x in adj_list[curr_route]:
                        if visted[x] == 0:
                            q.append(x)
                            visted[x] = 1
        return res if res < n + 1 else -1
