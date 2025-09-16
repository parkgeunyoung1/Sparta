def perm(idx, selected, now_cost):
    global min_cost
    if now_cost >= min_cost:   # 현재 비용이 이미 최소 비용보다 크면 가지치기 (더 볼 필요 없음)
        return
    if idx == N:               # 모든 열을 다 채운 경우 (끝까지 선택 완료)
        min_cost = min(now_cost, min_cost)  # 최소 비용 갱신
        return

    for j in range(N):         # 현재 열(idx)에서 행(j)을 선택
        if j not in selected:  # 아직 선택하지 않은 행이라면
            selected.append(j)  # 선택
            new_cost = now_cost + item[j][idx]  # 비용 누적
            perm(idx + 1, selected, new_cost)   # 다음 열로 이동
            selected.pop()       # 백트래킹 (선택 취소)
T = int(input())  # 테스트케이스 수
for tc in range(1, T+1):
    N = int(input())  # 행렬 크기
    item = [list(map(int, input().split()))for _ in range(N)]  # 비용 행렬 입력

    min_cost = 2000  # 충분히 큰 값으로 초기화 (예: N ≤ 15라면 더 크게 해야 안전)
    perm(0, [], 0)   # 열 0부터 시작, 선택된 행 없음, 현재 비용 0
    print(f'#{tc} {min_cost}')  # 결과 출력
