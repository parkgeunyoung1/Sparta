T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        m = i - 1  # 중심 좌표 먼저 구하기  (index)
        base = stone[m]  # 기준이 되는 돌의 색깔
        end = m + j      # 마지막으로 바뀔 돌
        if end > N:      # 마지막의 인덱스가 N보다 크면 N으로 고정시킨다
            end = N
        for pos in range(m, end): # 중심에서 마지막으로 바뀔 돌까지 돌을 뒤집어 준다
            stone[pos] = base

    stone = [str(num) for num in stone]
    print(f"#{tc} {' '.join(stone)}")