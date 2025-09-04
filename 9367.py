T = int(input())            # 테스트케이스 입력
for tc in range(1, T+1):       # 테스트케이스 반복
    N = int(input())                # N 입력
    carrot = list(map(int, input().split()))  # carrot에 당근 크기 입력
    max_count = 1           # 최대 카운트는 1
    count = 1               # 초기 카운트도 1
    for i in range(N-1):        # carrot의 i 를 비교
        if carrot[i] < carrot[i+1]: # 다음 인덱스와 비교해서 다음것이 크면
            count += 1              # 카운트 증가
            if count > max_count:   # 카운트가 최대 카운트를 넘으면
                max_count = count   # 최대 카운트 값에 카운트를 입력
        else:                       # 만약 다음것보다 크지 않으면
            count = 1               # 카운트를 초기화화

   print(f'#{tc} {max_count}')