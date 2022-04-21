import itertools

def find_position(next_position, weak):
    for idx, w in enumerate(weak):
        if next_position == w:
            return idx + 1
        elif next_position < w:
            return idx
    return len(weak)

def solution(n, weak, dist):
    answer = 1000
    all_cases = [case for case in itertools.permutations(range(len(dist)))]
    size_weak = len(weak)
    for _ in range(size_weak):
        for case in all_cases:
            current_position = weak[0]
            result = 0
            for worker in case:
                next_position = current_position + dist[worker]
                next_position_idx = find_position(next_position, weak)
                result += 1
                if next_position_idx >= len(weak):
                    break
                current_position = weak[next_position_idx]
            if next_position_idx < len(weak):
                result = 1000
            answer = min(answer, result)
            
        weak.append(weak[0] + n)
        del weak[0]
        
    if answer == 1000:
        answer = -1
    
    return answer