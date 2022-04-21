def solution(s):
    answer = 100000
    length = len(s)
    if length == 1:
        return 1
    maximum = int(length / 2)
    for i in range(1, maximum + 1):
        result_str = ""
        cutted = [s[(i*j):(i*(j+1))] for j in range(int(length / i))]
        if length % i != 0:
            cutted.append(s[(i*int(length/i)):])
        prev = cutted[0]
        count = 1
        for j in range(1, len(cutted)):
            if prev == cutted[j]:
                count += 1
            else:
                if count > 1:
                    result_str += str(count) + prev
                else:
                    result_str += prev
                count = 1
            prev = cutted[j]
            
        if count > 1:
            result_str += str(count) + prev
        else:
            result_str += prev
            
        if len(result_str) < answer:
            answer = len(result_str)
    
    return answer