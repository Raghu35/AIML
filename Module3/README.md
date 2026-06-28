# Module 3 — Advanced Python

Each notebook includes a **what / where / why** introduction (2–3 sentences) and runnable code with inline topic comments.

| # | Notebook | Topic |
|---|----------|-------|
| 01 | [01_multithreading.ipynb](01_multithreading.ipynb) | `threading`, locks, `ThreadPoolExecutor` |
| 02 | [02_multiprocessing.ipynb](02_multiprocessing.ipynb) | `Process`, `ProcessPoolExecutor`, `Queue` |
| 03 | [03_asyncio.ipynb](03_asyncio.ipynb) | `async`/`await`, tasks, timeouts, async context managers |
| 04 | [04_collections.ipynb](04_collections.ipynb) | Counter, defaultdict, deque, namedtuple, OrderedDict |
| 05 | [05_itertools.ipynb](05_itertools.ipynb) | permutations, combinations, groupby, chain, islice |
| 06 | [06_logging.ipynb](06_logging.ipynb) | levels, handlers, formatters, rotating logs |
| 07 | [07_dataclasses.ipynb](07_dataclasses.ipynb) | `@dataclass`, fields, frozen, ordering |
| 08 | [08_typing.ipynb](08_typing.ipynb) | Optional, Union, Callable, Generic, TypedDict |
| 09 | [09_performance.ipynb](09_performance.ipynb) | timeit, lru_cache, cProfile, concurrency choices |

Log files and profiling output go to [output/](output/).

**Note:** Multiprocessing notebooks use `if __name__ == "__main__":` guards required on Windows.
