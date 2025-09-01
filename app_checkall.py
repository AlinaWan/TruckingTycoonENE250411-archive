def find_all_paths(items, initial_rate):
    max_rate = max(rate for _, rate in items)
    targets = {i for i, (_, rate) in enumerate(items) if rate == max_rate}

    all_paths = []

    def dfs(current_rate, money, visited, path, score):
        for i, (cost, rate) in enumerate(items):
            if i in visited:
                continue
            if rate <= current_rate:
                continue  # Only allow upgrades

            time_to_buy = max(0, (cost - money) / current_rate)
            new_score = score + time_to_buy

            new_path = path + [i]
            new_visited = visited | {i}

            if i in targets:
                all_paths.append((new_path, new_score))

            # Continue exploring further upgrades
            dfs(rate, 0, new_visited, new_path, new_score)

    dfs(initial_rate, 0, set(), [], 0)

    # Sort paths by score (efficiency) from best to worst
    all_paths.sort(key=lambda x: x[1])

    return all_paths

if __name__ == "__main__":
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

    all_paths = find_all_paths(items, initial_rate)

    for rank, (path, score) in enumerate(all_paths, 1):
        stats = [items[i] for i in path]
        print(f"#{rank}: Path {path}, Stats: {stats}, Total Time: {score:.2f}")