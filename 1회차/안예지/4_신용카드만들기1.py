import sys

sys.stdin = open("_신용카드만들기1.txt")

# 신용카드-1
"""
16자리의 카드 번호 중 처음 15개가 주어졌을 때 룬 공식을 만족하가ㅣ 위해
마지막에 들어가는 숫자 N을 구하는 프로그램 작성

룬 공식
1) 홀수자리 숫자마다 2를 곱하여 더함
2) 짝수자리 숫자마다 그대로 더 함
3) 1)과 2)를 합한 숫자에 N을 더한 숫자가 10으로 나눠 떨어지면 유효한 숫자

# 입력
첫 번째 줄 테스트 케이스 수 T
각 줄에는 공백으로 구분한 자연수 15개

# 출력
16번째 자리에 들어가는 숫자를 찾아 출력

# 접근
1. 홀수와 짝수 자리의 범위를 분리해서 순회한다.
2. 홀,짝수의 더한 값을 10으로 나눈 나머지가 곧 N이 10을 위해 충족시켜야할 값이 되므로
3. 10에서 나머지를 빼준 값을 N에 할당한다.
4. 카드 번호는 한 자리이므로 N이 한 자리가 넘어갈 경우(나머지가 0인 경우
5. 끝 자리만 출력한다.

"""
T = int(input())
for _ in range (1, T+1):
    number = list(map(int, input().split()))
    # 홀수 자리의 합을 저장할 변수
    odd_ = 0
    # 짝수 자리의 합을 저장할 변수
    even_ = 0
    for i in range(0, len(number), 2):
        odd_ += number[i] * 2
    for j in range(1, len(number)-1, 2):
        even_ += number[j]
# print(list(range(0, len(number), 2)))
# print(list(range(1, len(number)-1, 2)))
# print(odd_ + even_)
    sum_ = odd_ + even_
    N = 10 - sum_%10
    # N은 한 자리 숫자여야 하므로 10이상일 경우 끝자리 수만 출력
    if N >= 10:
        N = str(N)[-1]
        # print(sum_%10)
    print(f'#{_} {N}')
# N = 10 - (odd_ + even_)%10
# print(N)