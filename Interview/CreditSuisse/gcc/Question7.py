from typing import List
from collections import defaultdict


def solution(n: int, l: int, transfers: List[List[int]]) -> bool:
    out_degree, in_degree = defaultdict(set), defaultdict(set)
    for source, destination in transfers:
        out_degree[source].add(destination)
        in_degree[destination].add(source)
    stack = [key for key, value in out_degree if value == 0]
    visited = set()

    while len(stack) != 0:
        curr_node = stack.pop()
        visited.add(curr_node)
        neighbours = in_degree[curr_node]

        for neighbour in neighbours:
            if neighbour in visited:
                continue
            neighbour_neighbours = out_degree[neighbour]
            neighbour_neighbours.remove(curr_node)
            if len(neighbour_neighbours) == 0:
                stack.append(neighbour)
            out_degree[neighbour] = neighbour_neighbours

        return len(visited) == n


def main():
    n, l = [int(i) for i in input().split(" ")]
    transfers = []
    for i in range(l):
        line = input().split(" ")
        transfers.append([int(line[0]), int(line[1])])

    result = solution(n, l, transfers)
    print("Ineligible" if result else "Eligible")


if __name__ == '__main__':
    main()
