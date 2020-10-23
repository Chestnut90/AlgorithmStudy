# 조이스틱
# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
#
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
#
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
# 예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.
#
# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
#
# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
# 입출력 예
# name	return
# JEROEN	56
# JAN	23
# 출처
#
# ※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
def dist(alphabet):
    from_a = ord(alphabet) - ord('A')
    if from_a < 14:
        return from_a
    return 26 - from_a

from collections import deque
def solution(name):
    answer = 0
    for n in name:
        answer += dist(n)

    temp = ['A' for n in name]
    min_length = len(name) - 1
    # bfs
    # [ string, count, index, direction ]
    queue = deque([[temp, 0, 0, 'r']])

    while queue:

        current, count, index, move = queue.popleft()
        current[index] = name[index]

        if count > min_length:
            continue

        if ''.join(current) == name:
            if count < min_length:
                min_length = count
                continue

        # right
        right = [n for n in current]
        right_index = index + 1
        if right_index == len(name):
            right_index = 0
        queue.append([right, count + 1, right_index, 'r'])

        # left
        left = [n for n in current]
        left_index = index - 1
        if left_index == -1:
            left_index = len(name) - 1
        queue.append([left, count + 1, left_index, 'l'])

    print(answer + min_length)
    return answer + min_length

if __name__ == '__main__':
    solution("JAZAAAZZZAAA")
    solution("JEROEN")















