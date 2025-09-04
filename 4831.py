T = int(input())            # 테스트케이스 입력
for tc in range(1, T+1):       # 테스트케이스 반복
    K, N, M = map(int,input().split())    # K, N, M 입력
    charger = list(map(int, input().split()))  # 충전소 위치 리스트
    total = [0] + charger + [N]             # 시작점과 종점 추가
    count = 0                       # 횟수
    current = 0                     # 현재위치 인덱스
    while current < M+1:            # 종점 인덱스(M+1) 도착까지 반복
        next_charger = current      # 다음 이동할 충전소 인덱스
        for i in range(current+1, M+2):     # 현재위치 다음부터 종점까지 확인
            if total[i] - total[current] <= K:  # 이동가능 거리가 K 이하면
                next_charger = i                    # 다음 충전소 인덱스는 i(가장 먼거리)
            else:                               # 거리가 이상이면 중단
                break
        if next_charger == current:             # 다음 충전소 인덱스가 현재 인덱스면 움직일 수 없기 때문에
            count = 0                           # 결과값이 0이 되고 종료
            break
        if next_charger != M+1:                 # 다음 충전소 인덱스가 종점이 아니면
            count += 1                          # 횟수를 추가하고
        current = next_charger                  # 현재인덱스를 다음 충전소 인덱스로 이동하고 반복
    print(f'#{tc} {count}')