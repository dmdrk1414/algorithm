# https://school.programmers.co.kr/learn/courses/30/lessons/250125#

def solution(board, h, w):
    n = len(board)
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]

        if (0 <= ny < n) and (0 <= nx < n):
            if board[h][w] == board[ny][nx]:
                count += 1
    answer = count
    return answer
