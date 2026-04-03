import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, None))

    came_from = {}
    g_cost = {start: 0}

    while open_list:
        f, g, current, parent = heapq.heappop(open_list)

        if current in came_from:
            continue

        came_from[current] = parent

        if current == goal:
            return reconstruct_path(came_from, goal), g

        for neighbor, cost in graph[current]:
            new_g = g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_new = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_new, new_g, neighbor, current))

    return None, float('inf')

def reconstruct_path(came_from, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]
    return path[::-1]


# ---------- USER INPUT ----------
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

print("\nEnter node names:")
nodes = []
for _ in range(n):
    node = input().strip()
    nodes.append(node)
    graph[node] = []

print("\nEnter heuristic value for each node:")
for node in nodes:
    heuristic[node] = int(input(f"h({node}) = "))

e = int(input("\nEnter number of edges: "))

print("\nEnter edges (from to cost):")
for _ in range(e):
    u, v, cost = input().split()
    graph[u].append((v, int(cost)))

start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

# ---------- RUN A* ----------
path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("\nPath:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
