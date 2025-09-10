def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr) - 1    # 검색 끝점
    last = 0                # 직전 탐색 방향을 기록  0: 없음 -1: 직전 왼쪽, 1: 직전 오른쪽

    while left <= right:  # 교차되면 못찾은 것
        mid = (left + right) // 2


        if arr[mid] == target:  # 가운데 원소 값이 찾는 값이면
            return True  # True로 return

        # target 보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:    # 타겟이 가운데 값보다 작으면 왼쪽 구간으로 이동
            if last == -1:      # 직전에도 왼쪽으로 갔으면 번갈아서 선택하는 조건을 충족이 안됨
                return False    # False로 반환
            last = -1           # 왼쪽으로 갔음을 표시
            right = mid - 1     # 오른쪽을 mid -1로 당겨서 왼쪽구간만 남김
        # target 보다 정답이 오른쪽에 있는 경우
        else:                      # 타겟이 가운데 값보다 크면 오른쪽으로 이동
            if last == 1:          # 직전에도 오른쪽으로 갔으면 조건 위배
                return False        # False로 반환
            last = 1                # 오른쪽으로 갔음을 표시  
            left = mid + 1          # 왼쪽 끝을 m+1로 밀어서 오른쪽 구간만 남김

    # 못찾은 경우
    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    arr = sorted(A)
    cnt = 0
    for i in B:
        if binary_search_while(i):   # B의 i가 A에서 찾았으면 cnt +1
            cnt += 1

    print(f'#{tc} {cnt}')
