def solution(food_times, k):
    answer = 0
    count = 0
    idx = -1
    prev = 0
    prev_count = 0
    max_idx = len(food_times) - 1
    food_sorted = sorted(food_times)
    while count < k:
        idx += 1
        if idx <= max_idx:
            prev_count = count
            count += (food_sorted[idx] - prev) * (max_idx - idx + 1)
            prev = food_sorted[idx]
        else:
            return -1
        
    if count == k:
        for i in range(len(food_times)):
            if food_times[i] > prev:
                answer = i + 1
                return answer
        return -1
    else:
        count = prev_count
        if idx == 0:
            prev = 0
        else:
            prev = food_sorted[idx - 1]
        diff = (k - count) % (max_idx - idx + 1)
        i = 0
        idx = 0
        while i <= diff:
            if food_times[idx] > prev:
                i += 1
            idx += 1
        answer = idx
    
    return answer