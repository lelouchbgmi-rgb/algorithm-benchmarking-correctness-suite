# Algorithm Benchmarking & Correctness Suite

A reviewable Python project demonstrating algorithm contracts, edge-case tests, reference cross-checks, and reproducible local benchmarking.

## Quick start

Python 3.10+ required.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
python benchmarks/run_benchmarks.py --size 50000 --queries 2000 --repeats 5
```

## Contents

- `src/algolab/algorithms.py`: binary search, two sum, BFS shortest path.
- `tests/`: edge cases and deterministic randomized checks.
- `benchmarks/`: compares binary search to a simple linear-search reference on the same deterministic workload.
- `docs/complexity.md`: complexity and interpretation.

## Contracts

- `binary_search` requires sorted input; duplicate matches may return any matching index.
- `two_sum` returns distinct indices or `None`.
- `bfs_shortest_path` returns a shortest path in an unweighted graph, or `None`. Nodes absent from the adjacency map have no outgoing edges.

## Limitations

This is a learning/portfolio project. The benchmark is not a controlled scientific study, and performance varies by environment and workload.

To document benchmark experiments, record the machine specifications, Python version, command used, workload size, number of repetitions, and measured results in `docs/experiment-notes.md`.

Only include results that you have actually measured. Do not invent performance numbers or draw conclusions from a single run.
