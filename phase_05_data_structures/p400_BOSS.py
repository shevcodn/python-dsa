from collections import deque


class CityMap:
    def __init__(self):
        self.graph = {}

    def add_road(self, city1, city2, distance):
        if city1 not in self.graph:
            self.graph[city1] = {}
        if city2 not in self.graph:
            self.graph[city2] = {}
        self.graph[city1][city2] = distance
        self.graph[city2][city1] = distance

    def shortest_path(self, start, end):
        import heapq
        distances = {start: 0}
        heap = [(0, start)]
        while heap:
            dist, city = heapq.heappop(heap)
            if city == end:
                return dist
            if dist > distances.get(city, float('inf')):
                continue
            for neighbor, d in self.graph.get(city, {}).items():
                new_dist = dist + d
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))
        return -1

    def all_reachable(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            city = queue.popleft()
            if city in visited:
                continue
            visited.add(city)
            for neighbor in self.graph.get(city, {}).keys():
                if neighbor not in visited:
                    queue.append(neighbor)
        return visited

    def most_connected(self):
        max_connections = 0
        most_connected_city = None
        for city, neighbors in self.graph.items():
            connections = len(neighbors)
            if connections > max_connections:
                max_connections = connections
                most_connected_city = city
        return most_connected_city

city = CityMap()
city.add_road("A", "B", 5)
city.add_road("B", "C", 3)
city.add_road("A", "C", 10)
city.add_road("C", "D", 2)

print(city.shortest_path("A", "D"))
print(city.all_reachable("A"))
print(city.most_connected())