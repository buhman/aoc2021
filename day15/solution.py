import heapq


def parse_input():
    with open('input.txt') as f:
        for line in f.read().split('\n'):
            if line:
                yield [int(i) for i in line]


def dijkstra(graph, source):
    vertex_set = []
    dist = dict()
    prev = dict()

    for y in range(len(graph)):
        for x in range(len(graph[0])):
            vertex = (x, y)
            dist[vertex] = None
            prev[vertex] = None
            vertex_set.append(vertex)
    dist[source] = 0

    heapq.heapify(vertex_set)

    def next_min_dist():
        return heapq.heappop(vertex_set)

    def neighbors(vertex):
        x, y = vertex
        if x > 0:
            yield (x - 1, y)
        if y > 0:
            yield (x, y - 1)
        if x < (len(graph) - 1):
            yield (x + 1, y)
        if y < (len(graph) - 1):
            yield (x, y + 1)

    #touched = False
    while vertex_set:
        if len(vertex_set) % 50 == 0:
            print(len(vertex_set))
        u_vertex = next_min_dist()
        vertex_set.remove(u_vertex)
        #u_vertex = vertex_set.pop()
        for neighbor in neighbors(u_vertex):
            if neighbor not in vertex_set:
                continue
            alt = dist[u_vertex] + graph[u_vertex[1]][u_vertex[0]]
            if not dist[neighbor] or alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = u_vertex
                touched = True
        #if touched:
        #    vertex_set.sort(key=lambda v: dist[v] if dist[v] is not None else 2 ** 32, reverse=True)
        #    touched = False

    return prev


def follow_path(weights, source, dest):
    vertex = dest
    while True:
        if vertex == source:
            return
        yield vertex
        vertex = weights[vertex]


def tile_graph(graph):
    new_graph = []
    for _ in range(len(graph) * 5):
        row = ([0] * len(graph[0]) * 5)
        new_graph.append(row)
    assert(len(new_graph) == len(graph) * 5)
    assert(len(new_graph[0]) == len(graph[0]) * 5)

    for ty in range(5):
        for y in range(len(graph)):
            for tx in range(5):
                for x in range(len(graph[0])):
                    next_risk = (graph[y][x] + (ty + tx))
                    while next_risk > 9:
                        next_risk = next_risk - 9
                    assert next_risk != 0
                    nx = len(graph[0]) * tx + x
                    ny = len(graph) * ty + y
                    new_graph[ny][nx] = next_risk
    return new_graph


def solution():
    graph = list(parse_input())
    source = (0, 0)
    dest = (len(graph) - 1, len(graph[0]) - 1)
    weights = dijkstra(graph, source)
    path = list(follow_path(weights, source, dest))
    risk = sum(graph[v[1]][v[0]] for v in path)
    print("part1", risk)

    tiled_graph = tile_graph(graph)
    weights = dijkstra(tiled_graph, source)
    tiled_dest = (len(tiled_graph) - 1, len(tiled_graph[0]) - 1)
    tiled_path = list(follow_path(weights, source, tiled_dest))
    tiled_risk = sum(tiled_graph[v[1]][v[0]] for v in tiled_path)
    print("part2", tiled_risk)

solution()
