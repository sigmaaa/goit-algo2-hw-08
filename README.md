
# Range Sum Optimization & Sliding Window Rate Limiter (goit-algo2-hw-08) Homework №8

This repository contains two independent Python tasks demonstrating optimization and rate limiting techniques.

---

## **Task 1 — Range Sum Optimization with LRU Cache**

### **Goal**

Show how an **LRU cache** improves performance for repeated range-sum queries on a large array.

### **Requirements**

* Input: array of `N` numbers and `Q` queries.
* Query types:

  * `Range(L, R)` → compute sum of elements in `array[L:R+1]`.
  * `Update(index, value)` → assign new value and invalidate affected cache entries.
* Implement:

  * `range_sum_no_cache()`
  * `update_no_cache()`
  * `range_sum_with_cache()` — uses ready-made `LRUCache`.
  * `update_with_cache()` — updates array and invalidates overlapping cached ranges.
* Use the provided workload generator (3% updates, 97% reads, 95% from “hot” intervals).
* Compare total runtime between non-cached and cached versions:

  ```
  Without cache: 12.06 s
  With LRU cache:  4.71 s  (speedup ×2.6)
  ```

### **Success Criteria**

* All functions implemented correctly.
* Code runs without errors.
* Results show measurable performance improvement.

---

## **Task 2 — Sliding Window Rate Limiter**

### **Goal**

Implement a **sliding window** rate limiter to control how frequently users can send messages.

### **Requirements**

* Parameters:

  * `window_size = 10s`
  * `max_requests = 1`
* Use `collections.deque` to store timestamps per user.
* Implement methods:

  * `_cleanup_window(user_id, current_time)` — remove outdated timestamps.
  * `can_send_message(user_id)` — check if a user can send.
  * `record_message(user_id)` — record new message if allowed.
  * `time_until_next_allowed(user_id)` — return wait time in seconds.
* Include a demo that simulates several users sending messages at random intervals.

### **Success Criteria**

* First message is always allowed.
* Sending again within 10 seconds is blocked.
* Expired records are automatically removed.
* `time_until_next_allowed()` returns correct waiting time.
* Test output matches expected rate-limiting behavior.

---

### **Author**

Denys Almazov
