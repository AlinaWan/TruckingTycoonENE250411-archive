def find_best_path(items, initial_rate):
    from collections import deque

    # Find all items with max income rate (most efficient targets)
    max_rate = max(rate for _, rate in items)
    targets = {i for i, (_, rate) in enumerate(items) if rate == max_rate}

    best_path = []
    min_score = float('inf')

    def dfs(current_rate, money, visited, path, score):
        nonlocal best_path, min_score

        for i, (cost, rate) in enumerate(items):
            if i in visited:
                continue
            if rate <= current_rate:
                continue  # Only allow rate increases

            time_to_buy = max(0, (cost - money) / current_rate)
            new_score = score + time_to_buy

            new_path = path + [i]
            new_visited = visited | {i}

            if rate == max_rate:
                if new_score < min_score:
                    min_score = new_score
                    best_path = new_path
            else:
                dfs(rate, 0, new_visited, new_path, new_score)

    # Start DFS from each item we can "buy" from initial rate
    dfs(initial_rate, 0, set(), [], 0)

    return best_path, min_score

if __name__ == "__main__":
    # Input your own dataset here: list of (cost, income rate)
    items = [
        (0, 65),
        (30000, 182),
        (52000, 222),
        (80000, 216),
        (142500, 696),
        (252500, 780),
        (320000, 780),
        (550000, 1032),
        (680000, 1620),
        (880000, 1890),
    ]

    initial_rate = 65

    best_path, total_score = find_best_path(items, initial_rate)

    print("Best acquisition path (by index):", best_path)
    print("Corresponding item stats:", [items[i] for i in best_path])
    print(f"Total efficiency score to reach most efficient item: {total_score:.2f}")