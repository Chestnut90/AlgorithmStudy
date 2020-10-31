# 등굣길
# 문제 설명
# 계속되는 폭우로 일부 지역이 물에 잠겼습니다.
# 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다.
# 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.
#
# 아래 그림은 m = 4, n = 3 인 경우입니다.
#
# image0.png
#
# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
#
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
# m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
# 물에 잠긴 지역은 0개 이상 10개 이하입니다.
# 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
# 입출력 예
# m	n	puddles	return
# 4	3	[[2, 2]]	4
# 입출력 예 설명
# image1.png

'''
timeout. -> O(2^n) --> O(2 ^(m*n))
'''
from collections import deque
def solution_bfs(m, n, puddles):

    puddles_set = set()
    for [a, b] in puddles:
        puddles_set.add((a-1, b-1))

    queue = deque([[0,0]])
    answer = 0
    while queue:
        cx, cy = queue.pop()

        if (cx, cy) in puddles_set:
            continue

        if cx == m - 1 and cy == n - 1:
            answer += 1
            continue

        # right
        nx, ny = cx + 1, cy
        if nx < m:
            queue.append([nx, ny])
        nx, ny = cx, cy + 1
        if ny < n:
            queue.append([nx, ny])

    return answer

def solution(m, n, puddles):
    roads = [[0 for i in range(m)] for j in range(n)]
    for x, y in puddles:
        roads[y-1][x-1] = -1
    for i in range(m):
        if roads[0][i] == -1:
            break
        roads[0][i] = 1
    for i in range(n):
        if roads[i][0] == -1:
            break
        roads[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if roads[i][j] == -1:
                continue
            add = 0 if roads[i][j-1] == -1 else roads[i][j-1]
            add += 0 if roads[i-1][j] == -1 else roads[i-1][j]
            roads[i][j] = add
    return roads[-1][-1] % 1000000007

def solution_blog(m, n, puddles):
    maps = [[0] * (m+1) for _ in range(n + 1)]
    maps[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                maps[i][j] = 0
            else:
                maps[i][j] += (maps[i-1][j] + maps[i][j-1])
    return maps[-1][-1] % 1000000007

if __name__ == '__main__':
    _m = 4
    _n = 3
    _puddles = [[2, 2]]
    _result = 4

    print(solution_blog(_m, _n, _puddles))

    print(solution(100, 100, []))
    print(solution(4, 2, []))