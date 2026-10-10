"""Algorithms with explicit contracts and input validation."""
from collections import deque
from collections.abc import Mapping, Sequence

def binary_search(sorted_values: Sequence[int], target: int) -> int | None:
    """Return a matching index in ascending input, or None. O(log n) time, O(1) space."""
    left, right = 0, len(sorted_values) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sorted_values[mid] == target: return mid
        if sorted_values[mid] < target: left = mid + 1
        else: right = mid - 1
    return None

def two_sum(values: Sequence[int], target: int) -> tuple[int, int] | None:
    """Return distinct indices summing to target, or None. Expected O(n) time and O(n) space."""
    seen: dict[int, int] = {}
    for j, value in enumerate(values):
        needed = target - value
        if needed in seen: return seen[needed], j
        seen.setdefault(value, j)
    return None

def bfs_shortest_path(graph: Mapping[str, Sequence[str]], start: str, goal: str) -> list[str] | None:
    """Return a shortest path in an unweighted graph, or None if unreachable. O(V+E)."""
    if not isinstance(start, str) or not isinstance(goal, str):
        raise ValueError("start and goal must be strings")
    if start == goal: return [start]
    queue = deque([start]); parent: dict[str, str | None] = {start: None}
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, ()):
            if not isinstance(neighbor, str): raise ValueError("graph neighbors must be strings")
            if neighbor in parent: continue
            parent[neighbor] = node
            if neighbor == goal:
                path = [goal]; cursor = goal
                while parent[cursor] is not None:
                    cursor = parent[cursor]  # type: ignore[assignment]
                    path.append(cursor)
                return path[::-1]
            queue.append(neighbor)
    return None
