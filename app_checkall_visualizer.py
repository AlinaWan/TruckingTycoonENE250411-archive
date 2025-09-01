import time

def find_all_paths(items, initial_rate, delay=0.5):
    max_rate = max(rate for _, rate in items)
    targets = {i for i, (_, rate) in enumerate(items) if rate == max_rate}
    all_paths = []

    def dfs(current_rate, money, visited, path, score, depth=0):
        indent = "  " * depth  # For tree visualization
        for i, (cost, rate) in enumerate(items):
            if i in visited:
                continue
            if rate <= current_rate:
                continue  # Only allow upgrades

            time_to_buy = max(0, (cost - money) / current_rate)
            new_score = score + time_to_buy
            new_path = path + [i]
            new_visited = visited | {i}

            print(f"{indent}Trying upgrade #{i} - Cost: {cost}, Rate: {rate}, Time to Buy: {time_to_buy:.2f}, New Total Time: {new_score:.2f}")
            print(f"{indent}Path so far: {new_path}\n")
            time.sleep(delay)

            if i in targets:
                all_paths.append((new_path, new_score))
                print(f"{indent}🎯 Target reached with path: {new_path}, Time: {new_score:.2f}\n")

            # Continue exploring further upgrades
            dfs(rate, 0, new_visited, new_path, new_score, depth + 1)

    dfs(initial_rate, 0, set(), [], 0)

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

    all_paths = find_all_paths(items, initial_rate, delay=0.5)

    print("\n==== All Paths ====\n")
    for rank, (path, score) in enumerate(all_paths, 1):
        stats = [items[i] for i in path]
        print(f"#{rank}: Path {path}, Stats: {stats}, Total Time: {score:.2f}")