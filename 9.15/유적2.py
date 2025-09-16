T = int(input())   # 사진 데이터 개수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0

    # 가로 탐색
    for i in range(N):
        count = 0
        for j in range(M):
            if grid[i][j] == 1:  # 가로로 연속되는 1 찾기
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0   # 1이 안나오면 0으로 초기화

    # 세로 탐색
    for j in range(M):
        count = 0
        for i in range(N):
            if grid[i][j] == 1:          # 세로로 연속되는 1 찾기
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0           # 1이 안나오면 0으로 초기화
    if max_count == 1:              # 최대가 2가 되야해서 1일경우는 0으로 바꿔줌-
        max_count = 0
    print(f'#{tc} {max_count}')
