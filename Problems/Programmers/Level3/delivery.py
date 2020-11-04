# 배달
# 문제 설명
# N개의 마을로 이루어진 나라가 있습니다. 이 나라의 각 마을에는 1부터 N까지의 번호가 각각 하나씩 부여되어 있습니다.
# 각 마을은 양방향으로 통행할 수 있는 도로로 연결되어 있는데, 서로 다른 마을 간에 이동할 때는 이 도로를 지나야 합니다.
# 도로를 지날 때 걸리는 시간은 도로별로 다릅니다. 현재 1번 마을에 있는 음식점에서 각 마을로 음식 배달을 하려고 합니다.
# 각 마을로부터 음식 주문을 받으려고 하는데, N개의 마을 중에서 K 시간 이하로 배달이 가능한 마을에서만 주문을 받으려고 합니다.
# 다음은 N = 5, K = 3인 경우의 예시입니다.
#
# image
#
# 위 그림에서 1번 마을에 있는 음식점은 [1, 2, 4, 5] 번 마을까지는 3 이하의 시간에 배달할 수 있습니다.
# 그러나 3번 마을까지는 3시간 이내로 배달할 수 있는 경로가 없으므로 3번 마을에서는 주문을 받지 않습니다.
# 따라서 1번 마을에 있는 음식점이 배달 주문을 받을 수 있는 마을은 4개가 됩니다.
# 마을의 개수 N, 각 마을을 연결하는 도로의 정보 road, 음식 배달이 가능한 시간 K가 매개변수로 주어질 때,
# 음식 주문을 받을 수 있는 마을의 개수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 마을의 개수 N은 1 이상 50 이하의 자연수입니다.
# road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
# road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
# road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
# a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
# 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
# 한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
# K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
# 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
# 1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.
# 입출력 예
# N	road	K	result
# 5	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	3	4
# 6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.
#
# 입출력 예 #2
# 주어진 마을과 도로의 모양은 아래 그림과 같습니다.
# image
# 1번 마을에서 배달에 4시간 이하가 걸리는 마을은 [1, 2, 3, 5] 4개이므로 4를 return 합니다.

class Town:
    def __init__(self, id):
        self.id = id
        self.near_town = {}
from collections import deque
'''
테스트 1 〉	통과 (0.09ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.08ms, 10.3MB)
테스트 13 〉	통과 (0.08ms, 10.3MB)
테스트 14 〉	통과 (0.98ms, 10.4MB)
테스트 15 〉	통과 (2.43ms, 10.6MB)
테스트 16 〉	통과 (0.05ms, 10.2MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.35ms, 10.3MB)
테스트 19 〉	통과 (1.05ms, 10.3MB)
테스트 20 〉	통과 (0.53ms, 10.3MB)
테스트 21 〉	통과 (1.37ms, 10.5MB)
테스트 22 〉	통과 (0.98ms, 10.2MB)
테스트 23 〉	통과 (2.76ms, 10.5MB)
테스트 24 〉	통과 (9.94ms, 10.3MB)
테스트 25 〉	통과 (1.73ms, 10.5MB)
테스트 26 〉	통과 (2.07ms, 10.5MB)
테스트 27 〉	통과 (2.55ms, 10.5MB)
테스트 28 〉	통과 (2.00ms, 10.7MB)
테스트 29 〉	통과 (8.08ms, 10.5MB)
테스트 30 〉	통과 (1.35ms, 10.6MB)
테스트 31 〉	통과 (0.12ms, 10.3MB)
테스트 32 〉	실패 (시간 초과)
'''
def solution_bfs(n, road, k):

    towns = [Town(i) for i in range(0, n + 1)]
    road.sort(key=lambda x:x[2], reverse=True)
    for a, b, c in road:
        town_a = towns[a]
        town_a.near_town[b] = c
        town_b = towns[b]
        town_b.near_town[a] = c

    answer = set()
    queue = deque([[1, 0, {1}]])
    while queue:
        town_id, time, visit = queue.pop()
        if time > k:
            continue

        answer.add(town_id)
        for t_id, t_road in towns[town_id].near_town.items():
            if t_id in visit:
                continue
            new_visit = set(visit)
            new_visit.add(t_id)
            queue.append([t_id, time + t_road, new_visit])

    return len(answer)

'''
dijkstra
'''
def solution(n, road, k):
    maps = [[0 if x == y else 500001 for x in range(n+1)] for y in range(n+1)]
    # make maps
    road.sort(key=lambda x:x[2], reverse=True)
    for a, b, c in road:
        maps[a][b] = c
        maps[b][a] = c

    start = 1
    visits = [False for _ in range(n+1)]
    visits[start] = True
    distances = list(maps[start])

    for _ in range(n-2):
        # select next node
        min_id, min_dis = -1, 500001
        for i, v in enumerate(distances[1:], start=1):
            if not visits[i] and min_dis > v:
                min_id = i
                min_dis = v
        # update
        start = min_id
        visits[start] = True
        for i in range(1, n+1):
            new_dis = maps[start][i] + distances[start]
            if not visits[i] and distances[i] > new_dis:
                distances[i] = new_dis

    return sum([0 if v > k else 1 for v in distances])

if __name__ == '__main__':

    _n = 5
    _road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    _k = 3
    _result = 4
    print(solution(_n, _road, _k))

    _n = 6
    _road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    _k = 4
    _result = 4
    print(solution(_n, _road, _k))

    _n = 7
    _road = [[1, 2, 5], [1, 6, 1], [2, 6, 1], [2, 3, 1], [3, 4, 2], [2, 5, 2], [1, 7, 3]]
    _k = 4
    print(solution(_n, _road, _k))
