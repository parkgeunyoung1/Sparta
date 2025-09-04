T = int(input())            # 테스트케이스 입력
for tc in range(1, T+1):       # 테스트케이스 반복
    N = int(input())                # N 입력
    nums = list(map(int, input()))  # 에 당근 크기 입력
    max_count = 0           # 최대 카운트는 1
    count = 0               # 초기 카운트도 1
    for i in range(N):          # 인덱스를 순서대로 순환
        if nums[i] == 1:        # 값이 1일때
            count += 1             # 카운트 증가
            if count > max_count:
                max_count = count        # 카운트가 최대 카운트를 넘으면
                                        # 최대 카운트 값에 카운트를 입력
        else:
            count = 0               # 1이 아니면 카운트를 초기화


    print(f'#{tc} {max_count}')