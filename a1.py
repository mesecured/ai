from queue import PriorityQueue

def heuristic(node, goal):
    
    (x1, y1) = node
    (x2, y2) = goal
    return ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5

def a_star_search(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    path = {start: []} 
    g_scores = {start: 0}  

    while not priority_queue.empty():
        (_, current_node) = priority_queue.get()

        if current_node == goal:
            return True, path[current_node] + [current_node]  

        visited.add(current_node)

        for (neighbor, neighbor_cost) in graph[current_node]:
            g_score = g_scores[current_node] + neighbor_cost

            if neighbor not in g_scores or g_score < g_scores[neighbor]:
                g_scores[neighbor] = g_score
                priority = g_score + heuristic(neighbor, goal)
                priority_queue.put((priority, neighbor))
                path[neighbor] = path[current_node] + [current_node]

    return False, []  



graph = {
    (0, 0): [((1, 0), 5), ((0, 1), 2)],
    (1, 0): [((0, 0), 5), ((2, 0), 1), ((1, 1), 6)],
    (0, 1): [((0, 0), 2), ((0, 2), 3)],
    (2, 0): [((1, 0), 1), ((2, 1), 4)],
    (1, 1): [((1, 0), 6), ((1, 2), 4)],
    (0, 2): [((0, 1), 3), ((1, 2), 4)],
    (2, 1): [((2, 0), 4), ((2, 2), 5)],
    (1, 2): [((1, 1), 4), ((0, 2), 4), ((2, 2), 3)],
    (2, 2): [((2, 1), 5), ((1, 2), 3)]
}

start_node = (0, 0)
goal_node = (2, 2)

result, path = a_star_search(graph, start_node, goal_node)

if result:
    print("Goal node is reachable.")
    print("Path:", ' -> '.join(map(str, path)))
else:
    print("Goal node is not reachable.")
