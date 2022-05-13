def split_bracket(brackets):
    stack = []
    stack.append(brackets[0])
    u_idx = len(brackets)
    if brackets[0] == '(':
        insert_bracket = '('
        delete_bracket = ')'
    else:
        insert_bracket = ')'
        delete_bracket = '('
    for i in range(1, len(brackets)):
        if not stack:
            u_idx = i
            break
        if brackets[i] == insert_bracket:
            stack.append(brackets[i])
        else:
            stack.pop()
    u = brackets[:u_idx]
    v = brackets[u_idx:]
    return u, v

def check_valid_bracket(brackets):
    if brackets == '':
        return True
    stack = []
    stack.append(brackets[0])
    if brackets[0] == ')':
        return False
    for i in range(1, len(brackets)):
        if brackets[i] == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    
    return True

def correct_bracket(brackets):
    answer = ''
    if brackets == '':
        return ''
    u, v = split_bracket(brackets)
    if check_valid_bracket(u):
        answer += u
        v = correct_bracket(v)
        answer += v
    else:
        answer = '('
        v = correct_bracket(v)
        answer += v
        answer += ')'
        u = u[1:-1]
        temp = ''
        for bracket in u:
            if bracket == '(':
                temp += ')'
            else:
                temp += '('
        answer += temp
    
    return answer

def solution(p):
    answer = ''
    answer = correct_bracket(p)
    
    return answer