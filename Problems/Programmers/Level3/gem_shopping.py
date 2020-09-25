# [카카오 인턴] 보석 쇼핑
# 문제 설명
# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
#
# 개발자 출신으로 세계 최고의 갑부가 된 어피치는 스트레스를 받을 때면 이를 풀기 위해 오프라인 매장에 쇼핑을 하러 가곤 합니다.
# 어피치는 쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있습니다.
# 어느 날 스트레스를 풀기 위해 보석 매장에 쇼핑을 하러 간 어피치는 이전처럼 진열대의 특정 범위의 보석을 모두 구매하되
# 특별히 아래 목적을 달성하고 싶었습니다.
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
#
# 예를 들어 아래 진열대는 4종류의 보석(RUBY, DIA, EMERALD, SAPPHIRE) 8개가 진열된 예시입니다.
#
# 진열대 번호	1	2	3	4	5	6	7	8
# 보석 이름	DIA	RUBY	RUBY	DIA	DIA	EMERALD	SAPPHIRE	DIA
# 진열대의 3번부터 7번까지 5개의 보석을 구매하면 모든 종류의 보석을 적어도 하나 이상씩 포함하게 됩니다.
#
# 진열대의 3, 4, 6, 7번의 보석만 구매하는 것은 중간에 특정 구간(5번)이 빠지게 되므로 어피치의 쇼핑 습관에 맞지 않습니다.
#
# 진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다.
# 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며,
# 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.
#
# [제한사항]
# gems 배열의 크기는 1 이상 100,000 이하입니다.
# gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
# gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
# gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.
# 입출력 예
# gems	result
# ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	[3, 7]
# ["AA", "AB", "AC", "AA", "AC"]	[1, 3]
# ["XYZ", "XYZ", "XYZ"]	[1, 1]
# ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]
# 입출력 예에 대한 설명
# 입출력 예 #1
# 문제 예시와 같습니다.
#
# 입출력 예 #2
# 3종류의 보석(AA, AB, AC)을 모두 포함하는 가장 짧은 구간은 [1, 3], [2, 4]가 있습니다.
# 시작 진열대 번호가 더 작은 [1, 3]을 return 해주어야 합니다.
#
# 입출력 예 #3
# 1종류의 보석(XYZ)을 포함하는 가장 짧은 구간은 [1, 1], [2, 2], [3, 3]이 있습니다.
# 시작 진열대 번호가 가장 작은 [1, 1]을 return 해주어야 합니다.
#
# 입출력 예 #4
# 4종류의 보석(ZZZ, YYY, NNNN, BBB)을 모두 포함하는 구간은 [1, 5]가 유일합니다.
# 그러므로 [1, 5]를 return 해주어야 합니다.
#
# ※ 공지 - 2020년 7월 21일 테스트케이스가 추가되었습니다.

'''
O(n**2) -> timeout.
'''
def solution_(gems):
    answer = []
    length = len(gems)
    all_gems = set(gems)
    searchs = [] # item : (start, end, all_gems:set, is_find)
    for i, gem in enumerate(gems):
        searchs.append([i, length, set(), False])

        for search in searchs:
            if search[3]:
                continue
            search[2].add(gem)
            if search[2] == all_gems:
                search[1] = i
                search[3] = True

        while searchs:
            if searchs[0][3] == True:
                answer.append(searchs.pop(0))
                continue
            break

    answer.sort(key= lambda x: x[1] - x[0])
    return [answer[0][0] + 1, answer[0][1] + 1]

'''
two point
O(n)

front, end : index.
bag : hashtable / dictionary. -> record count of gems
all_gems : all of gems

1. front를 증가시키며 해당 gem을 bag에 추가하고 카운팅. (없으면 생성)
2. if bag의 길이가 모든 gem의 길이와 같을 경우.
    -> end를 증가시키면서 해당 gem을 bag에서 제거하고, 해당 gem의 카운트가 0이되면 front, end의 길이를 계산해서 최소값 저장.

** gem은 길이가 1 ~ 10인 알파벳이며, gem의 갯수 제한도 없기 때문에 bag.keys() == all_gems의 연산량이 많음.
    -> k : 1 ~ 10 / n : 1 ~ 100000
    -> worst : k*n
    --> 길이 비교로. len(bag) == len(all_gems)
    --> all_gems : 1 ~ 100000

'''
def solution(gems):
    all_gems = set(gems)
    length = len(gems)
    front, end = 0, 0
    x, y, dist = 0, 0, length
    bag = dict()

    while front < length:
        front_gem = gems[front]
        if front_gem not in bag:
            bag[front_gem] = 0
        bag[front_gem] += 1

        if len(bag) == len(all_gems):
            if dist > (front - end):
                dist = front - end
                x, y = end + 1, front + 1
            while end < front:
                end_gem = gems[end]
                bag[end_gem] -= 1
                if bag[end_gem] == 0:
                    bag.pop(end_gem)
                    if dist > (front - end):
                        dist = front - end
                        x, y = end + 1, front + 1
                    end += 1
                    break
                end += 1
        front += 1

    return [x, y]

if __name__ == '__main__':

    _gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    _result = [3, 7]
    r = solution(_gems)
    print(r)

    _gems = ["AA", "AB", "AC", "AA", "AC"]
    _result = [1, 3]
    r = solution(_gems)
    print(r)

    _gems = ["XYZ", "XYZ", "XYZ"]
    _result = [1, 1]
    r = solution(_gems)
    print(r)

    _gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    _result = [1, 5]
    r = solution(_gems)
    print(r)