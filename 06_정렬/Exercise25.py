import copy

def solution(N, stages):
    answer = []
    stages_people = [0 for _ in range(N + 2)]
    for stage in stages:
        stages_people[stage] += 1
    total_people = copy.deepcopy(stages_people)
    for i in range(N, 0, -1):
        total_people[i] = total_people[i + 1] + total_people[i]
    del stages_people[0]
    del total_people[0]
    stages_people.pop()
    total_people.pop()
    ranking = [(idx + 1, stage / total) if total != 0 else (idx + 1, 0) for idx, (stage, total) in enumerate(zip(stages_people, total_people))]
    ranking.sort(key=lambda x: -x[1])
    answer = [stage_number for stage_number, _ in ranking]
    return answer