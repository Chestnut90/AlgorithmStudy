# 삼각 달팽이
# 문제 설명
#
# 정수 n이 매개변수로 주어집니다.
# 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
# 첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.
#
# examples.png
#
# 제한사항
# n은 1 이상 1,000 이하입니다.
# 입출력 예
# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
# 6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
# 입출력 예 #2
#
# 문제 예시와 같습니다.
# 입출력 예 #3
#
# 문제 예시와 같습니다.

'''
step : left-down / right / right-up

1) left-down
    next index = current index + current weight
    weight += 1

2) right
    next index = current index + 1
    weight = weight

3) right-up
    next index = current index - current weight
    weight -= 1

value += 1 in every step.
'''
def solution(n):
    total = n * (n + 1) // 2
    answer = [1] * total

    time = n
    index, value, weight = 0, 0, 0
    step = 'down'

    while time > 0:
        if step == 'down':
            for i in range(time):
                index += weight
                weight += 1
                value += 1
                answer[index] = value
            step = 'right'
        elif step == 'right':
            for i in range(time):
                index += 1
                value += 1
                answer[index] = value
            step = 'up'
        else:
            for i in range(time):
                index -= weight
                weight -= 1
                value += 1
                answer[index] = value
            step = 'down'
        time -= 1

    return answer

if __name__ == '__main__':
    _n = 5
    _result = [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
    r = solution(_n)
    print(r)