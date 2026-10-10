# Complexity and contract notes

| Algorithm | Time | Extra space | Assumption |
|---|---:|---:|---|
| Binary search | O(log n) | O(1) | Input sorted ascending |
| Two sum | Expected O(n) | O(n) | Hash map operations expected O(1) |
| BFS shortest path | O(V + E) | O(V) | Unweighted graph |

Tests include boundaries, duplicate values, unreachable nodes, invalid node types, and deterministic randomized cross-checks. Benchmark timings are local observations, not universal performance claims. Record your Python version, machine, and actual output before drawing conclusions.
