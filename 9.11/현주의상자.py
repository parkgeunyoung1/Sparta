T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * N           # 0이 써져있는 box 리스트 만들기
    for i in range(1, Q+1):  # 1~ Q 까지의 i 
        L, R = map(int, input().split())  # L, R 할당
        for x in range(L-1, R):  # 박스의 수를 바꿀 index 지정
            box[x] = i

    print(f'#{tc}', *box)
