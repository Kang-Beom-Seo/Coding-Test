from itertools import combinations

N, M = map(int, input().split())
cities_map = [[i for i in map(int, input().split())] for _ in range(N)]
chicken_map = [(i, j) for i in range(N) for j in range(N) if cities_map[i][j] == 2]
house_map = [(i, j) for i in range(N) for j in range(N) if cities_map[i][j] == 1]
MAX = 10000
answer = MAX

for chickens in combinations(chicken_map, M):
    distance_list = [MAX for _ in range(len(house_map))]
    for idx, house in enumerate(house_map):
        for chicken in chickens:
            distance = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
            distance_list[idx] = min(distance_list[idx], distance)
    now_distance = sum(distance_list)
    answer = min(answer, now_distance)
print(answer)