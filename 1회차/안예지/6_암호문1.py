import sys

sys.stdin = open("_암호문1.txt")

# 암호문 -1
"""
I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. 
s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]

# 입력
첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수)

두 번째 줄 : 원본 암호문

세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수)

네 번째 줄 : 명령어

# 출력
# 기호와 함께 테스트 케이스의 번호를 출력하고, 
공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.

# 접근
1. 명령어가 삽입 될때마다 값을 추가해야 하므로 리스트를 활용한다.
2. 'I'를 기점으로 x, y, 추가할 숫자의 시작 인덱스가 주어지므로 만날 때마다 재정의한다.
3. x위치에 y만큼의 숫자를 명령어 목록에서 가져와서 추가한다.
4. 다음 번째 'I'를 만나기 전까지 그 이후 숫자들을 x의 다음 위치에 계속 추가해야하므로
5. 값을 하나 추가할 때마다 x와 값을 추가할 인덱스를 1씩 증가시킨다.

"""
for _ in range(1, 11):
    
    N = int(input())
    pwlist = input().split()
    order_n = int(input())
    order = input().split()

    for idx in range(len(order)):
            if order[idx] == 'I':
                # 삽입할 인덱스를 저장할 변수
                    x = int(order[idx + 1]) 
                    # 삽입할 숫자의 개수를 저장할 변수
                    y = int(order[idx + 2])
                    for i in range(y):
                            pwlist.insert(x, order[idx + 3])
                            x += 1
                            idx += 1
    word = ''
    for j in range(10):
        word += pwlist[j] + " "
    print(f'#{_} {word}')