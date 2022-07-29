import sys

sys.stdin = open("_최빈수구하기.txt")

# 최빈수 구하기
"""
10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
위와 같은 수 분포에서 최빈수는 가장 여러 번 나타나는 값으로,
8이 된다. 최빈수를 출력하는 프로그램을 작성하라.
단, 최빈수가 여러 개 일대에는 가장 큰 점수를 출력하라.
학생의 수는 1천 명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.

# 입력
테스트케이스 T가 주어진다.
그 다음 줄부터 점수가 주어진다.

# 출력
# 부호와 함께 테스트 케이스의 번호를 출력하고,
공백 문자 후 테스트 케이스에 대한 답을 출력

# 접근
1. 딕셔너리로 접근
2. 점수에 대한 딕셔너리를 만들고 가장 많은 value가 나온 값에 해당하는 key를
3. 딕셔너리의 key와 비교하여 가장 큰 정수의 key를 출력

"""
T = int(input())
# 입력값 받아오기
for _ in range(T):
    T_number = int(input())
    # 점수 리스트 변수
    score = map(int, input().split())
    # 점수와 등장 빈도를 저장할 딕셔너리 생성
    score_dict = {}
    for i in score:
        # 점수 - 등장빈도 쌍의 딕셔너리 생성
        score_dict[i] = score_dict.get(i, 0) + 1
        # 등장빈도 중 가장 높은 값을 저장할 변수
        m_cnt = max(score_dict.values())
        # 최빈'값'들의 'key' 를 저장할 리스트
        k_list =[]
        for key in score_dict:
            if score_dict[key] == m_cnt:
                k_list.append(key)
    # print(k_list)
    print(f'#{T_number} {max(k_list)}')
    
