# 가장 긴 팰린드롬
# 문제 설명
# 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
# 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
#
# 예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.
#
# 제한사항
# 문자열 s의 길이 : 2,500 이하의 자연수
# 문자열 s는 알파벳 소문자로만 구성
# 입출력 예
# s	answer
# abcdcba	7
# abacde	3
# 입출력 예 설명
# 입출력 예 #1
# 4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.
#
# 입출력 예 #2
# 2번째자리 'b'를 기준으로 aba가 팰린드롬이 되므로 3을 return합니다.
'''

case 1.
if substring == substring[::-1]
효율성  테스트
테스트 1 〉	통과 (4747.06ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)

case 2.
if front == end:
효율성  테스트
테스트 1 〉	통과 (2583.16ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)

take much time when compare long string.
'''
def solution(s):
    answer = 1
    length = len(s)
    for i in range(length - 1, 1, -1):
        for j in range(length - i):
            substring = s[j:j+i+1]
            mid = len(substring)//2
            front = substring[:mid]
            end = substring[mid:][::-1] if len(substring) % 2 == 0 else substring[mid + 1:][::-1]
            if front == end:
                return len(substring)
    return answer

'''
other solution 
recursive.
'''
def longest_palindrom(s):
    # 함수를 완성하세요
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))

if __name__ == '__main__':
    _s = "abcdcba"
    _result = 7
    print(longest_palindrom(_s))

    _s = "abacde"
    _result = 3
    print(longest_palindrom(_s))