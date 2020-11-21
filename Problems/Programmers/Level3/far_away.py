# 멀리 뛰기
# 문제 설명
# 효진이는 멀리 뛰기를 연습하고 있습니다.
# 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다.
# 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다.
# 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내,
# 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요.
# 예를 들어 4가 입력된다면, 5를 return하면 됩니다.
#
# 제한 사항
# n은 1 이상, 2000 이하인 정수입니다.
# 입출력 예
# n	result
# 4	5
# 3	3
# 입출력 예 설명
# 입출력 예 #1
# 위에서 설명한 내용과 같습니다.
#
# 입출력 예 #2
# (2칸, 1칸)
# (1칸, 2칸)
# (1칸, 1칸, 1칸)
# 총 3가지 방법으로 멀리 뛸 수 있습니다.

import time

def solution(n):
    prev = [1, 2, 3]
    for i in range(n - 3):
        prev.append((prev[-1] + prev[-2]) % 1234567)
    return prev[n-1]

# binary.
def solution_recursive(n):
    return (solution_recursive(n - 1) + solution_recursive(n - 2)) % 1234567 if n > 2 else n

if __name__ == '__main__':
    _n = 50
    start = time.time()
    a = solution(_n)
    end = time.time()
    print(a)
    print(end - start)

    start = time.time()
    a = solution_recursive(_n)
    end = time.time()
    print(a)
    print(end - start)