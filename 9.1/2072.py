T = int(input())                # 첫번째 줄 T 를 할당
for tc in range(1, T+1):        # tc를 1~ T 까지 순회
    num = list(map(int, input().split())) # 숫자열 할당
    num_sum = 0   # 초기 숫자합
    for i in num:   # 숫자열 순회
        if i % 2 == 1: # 홀수인 숫자 일 때 숫자 더하기
            num_sum += i

    print(f'#{tc} {num_sum}')
