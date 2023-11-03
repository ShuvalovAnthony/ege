from collections import defaultdict

f = open('vars/shag/data2.txt')

n = int(f.readline())

tickets = []

for row in f:
    tickets.append(row.replace('\n', '').split('|'))


def find_longest_flight_path(graph, node, path):
    if node not in graph:
        return path
    longest_path = path
    for neighbor in graph[node]:
        if neighbor not in path:
            new_path = find_longest_flight_path(graph, neighbor, path + [neighbor])
            if len(new_path) > len(longest_path):
                longest_path = new_path
    return longest_path


graph = defaultdict(list)
for flight in tickets:
    departure, destination = flight
    graph[departure].append(destination)


max_paths = []
max_len = 0
for node in graph:
    path = find_longest_flight_path(graph, node, [node])
    if len(path) > max_len:
        max_paths = [path]
        max_len = len(path)
    elif len(path) == max_len:
        max_paths.append(path)


print(len(max_paths))
for path in sorted(max_paths, key=lambda x: x[0]):
    print('|'.join(path))