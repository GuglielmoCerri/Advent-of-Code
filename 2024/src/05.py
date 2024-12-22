from collections import defaultdict, deque

from lib.aoc import aoc

def is_update_valid(update, rules):
        index_map = {page: idx for idx, page in enumerate(update)}
        for x, y in rules:
            if x in index_map and y in index_map:
                if index_map[x] > index_map[y]:
                    return False
        return True

def get_middle_page(update):
    n = len(update)
    return update[n // 2]

def topological_sort(update, rules):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        update_set = set(update)

        for x, y in rules:
            if x in update_set and y in update_set:
                graph[x].append(y)
                in_degree[y] += 1
                in_degree.setdefault(x, 0)

        queue = deque([node for node in update if in_degree[node] == 0])
        sorted_update = []

        while queue:
            node = queue.popleft()
            sorted_update.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted_update

@aoc(5, 2024, 1)
def p1(indata: str) -> int:
    rules_section, updates_section = indata.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

    res = 0

    for update in updates:
        if is_update_valid(update, rules):
            res += get_middle_page(update)

    return res

@aoc(5, 2024, 2)
def p2(indata: str) -> int:

    rules_section, updates_section = indata.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]

    res = 0

    for update in updates:
        if not is_update_valid(update, rules):
            corrected_update = topological_sort(update, rules)
            res += get_middle_page(corrected_update)

    return res

if __name__ == "__main__":
    p1()
    p2()
