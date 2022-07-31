import sys

sys.stdin = open("_문자열의거울상.txt")

# 문자열의 거울상
"""
‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 
이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

# 입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다. 
문자열의 길이는 1이상 1000이하이다.

# 출력
각 테스트 케이스마다 주어진 문자열을 거울에 비춘 문자열로 출력한다.

# 접근
1. 문자열 하나에 대한 값을 바꿔야되므로
2. 변경 가능한 자료 구조 리스트로 접근(문자열.replace는 한 번에 바꾸기 때문에)
3. 리스트의 인덱스로 접근하여 변경한 문자열을 리스트로 저장하기
4. 다시 문자열로 합쳐서 출력하기

"""
T = int(input())
for _ in range(1, T + 1):
    word = input()
    # 새로운 문자열을 저장할 리스트 생성(인덱스 오류 방지)
    n_word = [0] * len(word)
    for idx in range(len(word)):
        # 해당 인덱스의 값이 '문자'일 때 변경할 '문자'를 리스트에 추가
        if word[idx] == 'b':
            n_word[idx] = 'd'
        if word[idx] == 'd':
            n_word[idx] = 'b'
        if word[idx] == 'p':
            n_word[idx] = 'q'
        if word[idx] == 'q':
            n_word[idx] = 'p'
    # 리스트 요소를 역순으로 정렬
    n_word.reverse()
    answer = ''
    for i in n_word:
        answer += i
    print(f'#{_} {answer}')