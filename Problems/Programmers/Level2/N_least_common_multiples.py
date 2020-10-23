# N개의 최소공배수
# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다.
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
#
# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.
# 입출력 예
# arr	result
# [2,6,8,14]	168
# [1,2,3]	6

'''
Greatest common divisor
'''
def gcd(a, b):
    # builtin function.
    # from math import gcd as _gcd

    if b == 0:
        return a
    else:
        return gcd(b, a%b)
'''
Least common multiple.
'''
def lcm(a, b):
    return a * b // gcd(a, b)

def solution_simple(arr):
    n = arr[0]
    for v in arr[1:]:
        n = lcm(n, v)
    return n

def solution(arr):
    def primes(n):
        temp = set(range(2, n + 1))
        _primes = set()
        while temp:
            a = temp.pop()
            if a not in _primes:
                sub = set(range(a, n + 1, a))
                temp = temp.difference(sub)
                _primes.add(a)
        return _primes

    def interger_factorization(n, primes):
        multiples = {}
        index = 0
        while index < len(primes):
            if n == 1:
                break

            prime = primes[index]
            if n % prime == 0:
                if prime not in multiples:
                    multiples[prime] = 0
                multiples[prime] += 1
                n = n // prime
                continue
            index += 1
        return multiples

    prime_numbers = list(primes(100))
    multiples = {}
    for n in arr:
        _mul = interger_factorization(n, prime_numbers)
        for key, value in _mul.items():
            if key not in multiples:
                multiples[key] = value
                continue
            if multiples[key] < value:
                multiples[key] = value
    answer = 1
    for key, value in multiples.items():
        answer *= (key ** value)
    return answer

if __name__ == '__main__':

    _arr = [2, 6, 8, 14]
    _result = 168
    r = solution(_arr)
    print(r)

    _arr = [1,2,3]
    _result = 6
    r = solution(_arr)
    print(r)

    print(gcd(2, 5))
    print(lcm(2, 5))