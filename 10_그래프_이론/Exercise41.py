def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [i for i in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]

for now_idx, node in enumerate(graph):
    for next_idx, isconnected in enumerate(node):
        if isconnected == 1:
            union_parent(parent, now_idx, next_idx)

plan = list(map(int, input().split()))
all_parents = [find_parent(parent, node - 1) for node in plan]

if len(set(all_parents)) == 1:
    print("YES")
else:
    print("NO")