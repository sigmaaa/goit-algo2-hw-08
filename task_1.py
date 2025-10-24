from functools import lru_cache
from collections import OrderedDict
import random
import time


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def make_queries(n, q, hot_pool=30, p_hot=0.95, p_update=0.03):
    hot = [
        (random.randint(0, n // 2), random.randint(n // 2, n - 1))
        for _ in range(hot_pool)
    ]
    queries = []
    for _ in range(q):
        if random.random() < p_update:  # ~3% запитів — Update
            idx = random.randint(0, n - 1)
            val = random.randint(1, 100)
            queries.append(("Update", idx, val))
        else:  # ~97% — Range
            if random.random() < p_hot:  # 95% — «гарячі» діапазони
                left, right = random.choice(hot)
            else:  # 5% — випадкові діапазони
                left = random.randint(0, n - 1)
                right = random.randint(left, n - 1)
            queries.append(("Range", left, right))
    return queries


def range_sum_no_cache(array, left, right):
    return sum(array[left : right + 1])


def update_no_cache(array, index, value):
    array[index] = value


def range_sum_with_cache(array, left, right, cache):
    key = (left, right)
    result = cache.get(key)
    if result != -1:
        return result
    result = sum(array[left : right + 1])
    cache.put(key, result)
    return result


def update_with_cache(array, index, value, cache: LRUCache):
    array[index] = value
    cache_keys = cache.cache.keys()
    for l, r in list(cache_keys):
        if l <= index <= r:
            del cache.cache[(l, r)]


def run(array, queries, range_sum_fn, update_fn, cache=None):
    arr = array.copy()
    start = time.time()
    for q in queries:
        if q[0] == "Range":
            (
                range_sum_fn(arr, q[1], q[2], cache)
                if cache
                else range_sum_fn(arr, q[1], q[2])
            )
        else:
            update_fn(arr, q[1], q[2], cache) if cache else update_fn(arr, q[1], q[2])
    return time.time() - start


if __name__ == "__main__":
    N = 100_000
    array = [random.randint(1, 100) for _ in range(N)]
    Q = 50_000
    queries = make_queries(N, Q)

    # Run without cache
    time_no_cache = run(array, queries, range_sum_no_cache, update_no_cache)

    # Run with LRU cache
    cache = LRUCache(1000)
    time_with_cache = run(
        array, queries, range_sum_with_cache, update_with_cache, cache
    )

    print(f"Без кешу : {time_no_cache:.2f} с")
    print(
        f"LRU-кеш  : {time_with_cache:.2f} с  (прискорення ×{time_no_cache / time_with_cache:.2f})"
    )
