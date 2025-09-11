T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]  # board에 숫자 받아오기
    turn_90 = [[0] * N for _ in range(N)]          # 90도, 180도, 270도 회전시킨걸 저장할 리스트 생성
    turn_180 = [[0] * N for _ in range(N)]
    turn_270 = [[0] * N for _ in range(N)]
    for i in range(N):                             # board 를 90도 회전, i,j -> j,N-1-i
        for j in range(N):
            turn_90[j][N-1-i] = board[i][j]

    for i in range(N):                             # turn_90 를 90도 회전, i,j -> j,N-1-i
        for j in range(N):
            turn_180[j][N - 1 - i] = turn_90[i][j]

    for i in range(N):                              # turn_180 를 90도 회전, i,j -> j,N-1-i
        for j in range(N):
            turn_270[j][N - 1 - i] = turn_180[i][j]

    print(f'#{tc}')
    for i in range(N):                              # 대괄호를 때고 문자열로 바꿔서 정렬
        s90 = ''.join(map(str, turn_90[i]))
        s180 = ''.join(map(str, turn_180[i]))
        s270 = ''.join(map(str, turn_270[i]))
        print(s90, s180, s270)
