# JadenCase 문자열 만들기
# 문제 설명
# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
#
# 제한 조건
# s는 길이 1 이상인 문자열입니다.
# s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
# 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
# 입출력 예
# s	return
# 3people unFollowed me	3people Unfollowed Me
# for the last week	For The Last Week

def solution(s):
    string = []
    isUpcase = True

    for c in s:
        if c == " ":
            isUpcase = True
        else:
            if isUpcase:
                isUpcase = False
                c = c.upper() if c.isalpha() else c
            else:
                c = c.lower() if c.isalpha() else c

        string.append(c)

    return ''.join(string)

def solution_title(s):
    '''
    str.title() function.
    ex)
    '3people unFollowed me' -> '3People Unfollowed Me' # wrong -> '3P'
    '''
    return s.title()

if __name__ == '__main__':
    _s = "3people unFollowed me"
    _result = "3people Unfollowed Me"
    r = solution(_s)
    print(r)

    _s = "for the last week"
    _result = "For The Last Week"
    r = solution(_s)
    print(r)

    _s = "for the last  week"
    _result = "For The Last  Week"
    r = solution(_s)
    print(r)

    print('test')
    test = []
    test.append('3people unFollowed me')
    test.append('For the last week')
    test.append('hello world.  two empty space.')
    for t in test:
        print(t.lower().title())

