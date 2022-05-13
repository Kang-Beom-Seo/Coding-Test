from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_valid(node, row, col):
    x, y = node
    return (x >= 0 and x < row and y >= 0 and y < col)

def is_rotation_possible(graph, row_visited, col_visited, center_point, other_point, row, col, direction, isrow):
    if isrow:
        if direction == 0:
            next_other_point = (center_point[0] - 1, center_point[1])
            quarter_point = (next_other_point[0], other_point[1])
            if check_valid(next_other_point, row, col) and check_valid(quarter_point, row, col) and graph[quarter_point[0]][quarter_point[1]] == 0 and graph[next_other_point[0]][next_other_point[1]] == 0 and not col_visited[next_other_point[0]][next_other_point[1]]:
                return (next_other_point, center_point)
            else:
                return False
        else:
            next_other_point = (center_point[0] + 1, center_point[1])
            quarter_point = (next_other_point[0], other_point[1])
            if check_valid(next_other_point, row, col) and check_valid(quarter_point, row, col) and graph[quarter_point[0]][quarter_point[1]] == 0 and graph[next_other_point[0]][next_other_point[1]] == 0 and not col_visited[center_point[0]][center_point[1]]:
                return (center_point, next_other_point)
            else:
                return False
    else:
        if direction == 0:
            next_other_point = (center_point[0], center_point[1] + 1)
            quarter_point = (other_point[0], next_other_point[1])
            if check_valid(next_other_point, row, col) and check_valid(quarter_point, row, col) and graph[quarter_point[0]][quarter_point[1]] == 0 and graph[next_other_point[0]][next_other_point[1]] == 0 and not row_visited[center_point[0]][center_point[1]]:
                return (center_point, next_other_point)
            else:
                return False
        else:
            next_other_point = (center_point[0], center_point[1] - 1)
            quarter_point = (other_point[0], next_other_point[1])
            if check_valid(next_other_point, row, col) and check_valid(quarter_point, row, col) and graph[quarter_point[0]][quarter_point[1]] == 0 and graph[next_other_point[0]][next_other_point[1]] == 0 and not row_visited[next_other_point[0]][next_other_point[1]]:
                return (next_other_point, center_point)
            else:
                return False

def bfs(graph, node, row_visited, col_visited):
    first_point, second_point = node
    row_visited[first_point[0]][first_point[1]] = True
    row = len(graph)
    col = len(graph[0])
    queue = deque()
    time = 0
    queue.append((first_point, second_point, time))
    while queue:
        first_point, second_point, time = queue.popleft()
        if second_point[0] == row - 1 and second_point[1] == col - 1:
            return time
        if first_point[0] == second_point[0]:
            isrow = True
        else:
            isrow = False
        for i in range(4):
            n_first_point = (first_point[0] + dx[i], first_point[1] + dy[i])
            n_second_point = (second_point[0] + dx[i], second_point[1] + dy[i])
            if check_valid(n_first_point, row, col) and check_valid(n_second_point, row, col) and graph[n_first_point[0]][n_first_point[1]] == 0 and graph[n_second_point[0]][n_second_point[1]] == 0:
                if isrow and not row_visited[n_first_point[0]][n_first_point[1]]:
                    row_visited[n_first_point[0]][n_first_point[1]] = True
                    queue.append((n_first_point, n_second_point, time + 1))
                elif not isrow and not col_visited[n_first_point[0]][n_first_point[1]]:
                    col_visited[n_first_point[0]][n_first_point[1]] = True
                    queue.append((n_first_point, n_second_point, time + 1))
        for i in range(2):
            rotated_point = is_rotation_possible(graph, row_visited, col_visited, first_point, second_point, row, col, i, isrow)
            if rotated_point:
                if isrow:
                    col_visited[rotated_point[0][0]][rotated_point[0][1]] = True
                else:
                    row_visited[rotated_point[0][0]][rotated_point[0][1]] = True
                queue.append((*rotated_point, time + 1))
        
        for i in range(2):
            rotated_point = is_rotation_possible(graph, row_visited, col_visited, second_point, first_point, row, col, i, isrow)
            if rotated_point:
                if isrow:
                    col_visited[rotated_point[0][0]][rotated_point[0][1]] = True
                else:
                    row_visited[rotated_point[0][0]][rotated_point[0][1]] = True
                queue.append((*rotated_point, time + 1))
    

def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    row_visited = [[False for _ in range(col)] for _ in range(row)]
    col_visited = [[False for _ in range(col)] for _ in range(row)]
    answer = bfs(board, ((0, 0), (0, 1)), row_visited, col_visited)
    
    return answer