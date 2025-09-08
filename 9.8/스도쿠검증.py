T = int(input())
for tc in range(1, T+1):
    board = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 판 만들기
    result = 1                  # 초기 결과값은 1(이상없을때)
    for r in range(9):          # 행 검사
        seen = [0] * 10
        for c in range(9):
            v = board[r][c]
            if v < 1 or v > 9 or seen[v]:       # 값이 1~9를 벗어나거나 중복이 됬을때 결과값을 0으로 하고 종료
                result = 0
                break
            else:
                seen[v] = 1                         # 아니면 값을 seem의 인덱스로 삼아 1로 표기(추후에 중복되면 종료)
    for r in range(9):                           # 열 검사
        seen = [0] * 10
        for c in range(9):
            v = board[c][r]
            if v < 1 or v > 9 or seen[v]:         # 값이 1~9를 벗어나거나 중복이 됬을때 결과값을 0으로 하고 종료
                result = 0
                break
            else:
                seen[v] = 1                            # 아니면 값을 seem의 인덱스로 삼아 1로 표기(추후에 중복되면 종료)

    for r in range(0, 9, 3):                    # 3X3 행렬 검사
        for c in range(0, 9, 3):                # 3X3 행렬 시작점 설정
            seen = [0] * 10                     # 시작점으로부터 3칸씩 검사
            for dr in range(3):
                for dc in range(3):
                    v = board[r+dr][c+dc]
                    if v < 1 or v > 9 or seen[v]:         # 값이 1~9를 벗어나거나 중복이 됬을때 결과값을 0으로 하고 종료
                        result = 0
                        break
                    else:
                        seen[v] = 1                           # 아니면 값을 seem의 인덱스로 삼아 1로 표기(추후에 중복되면 종료)


    print(f'#{tc} {result}')
