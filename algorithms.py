from collections import deque
import heapq

def in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height

def passable(x, y, walls):
    return (x, y) not in walls

def neighbors(cell, width, height, walls):
    x, y = cell
    nbrs = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    return [(nx, ny) for (nx, ny) in nbrs if in_bounds(nx, ny, width, height) and passable(nx, ny, walls)]

def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return []
    cur = goal
    path = [cur]
    while cur != start:
        cur = came_from[cur]
        path.append(cur)
    path.reverse()
    return path

def bfs(start, goal, width, height, walls):
    frontier = deque([start])
    came_from = {start: start}
    while frontier:
        cur = frontier.popleft()
        if cur == goal:
            break
        for nxt in neighbors(cur, width, height, walls):
            if nxt not in came_from:
                came_from[nxt] = cur
                frontier.append(nxt)
    return reconstruct_path(came_from, start, goal)

def dfs(start, goal, width, height, walls):
    frontier = [start]
    came_from = {start: start}
    while frontier:
        cur = frontier.pop()
        if cur == goal:
            break
        for nxt in neighbors(cur, width, height, walls):
            if nxt not in came_from:
                came_from[nxt] = cur
                frontier.append(nxt)
    return reconstruct_path(came_from, start, goal)

def ucs(start, goal, width, height, walls):
    frontier = [(0, start)]
    came_from = {start: start}
    cost_so_far = {start: 0}
    while frontier:
        cost, cur = heapq.heappop(frontier)
        if cur == goal:
            break
        for nxt in neighbors(cur, width, height, walls):
            new_cost = cost_so_far[cur] + 1
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                came_from[nxt] = cur
                heapq.heappush(frontier, (new_cost, nxt))
    return reconstruct_path(came_from, start, goal)

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal, width, height, walls):
    frontier = [(0, start)]
    came_from = {start: start}
    cost_so_far = {start: 0}
    while frontier:
        _, cur = heapq.heappop(frontier)
        if cur == goal:
            break
        for nxt in neighbors(cur, width, height, walls):
            new_cost = cost_so_far[cur] + 1
            if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                cost_so_far[nxt] = new_cost
                came_from[nxt] = cur
                priority = new_cost + manhattan(nxt, goal)
                heapq.heappush(frontier, (priority, nxt))
    return reconstruct_path(came_from, start, goal)
