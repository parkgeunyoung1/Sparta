T = int(input())            # 테스트케이스 입력
for tc in range(1, T+1):       # 테스트케이스 반복
    N = int(input())                # N 입력
    nums = list(map(int,input().split()))  # 정수 입력
    stack = []                  # 계산값을 넣을 리스트 생성
    max_num = -1                     # 최대 값 (곱이 없을 때 -1 로 출력)
    for i in range(N-1):            # nums에 있는 정수 값을 서로 곱하는데 같은 정수끼리나 같은 계산을 할 필요가 없어서 제외
        for j in range(i + 1, N):   # i는 N-1 설정(j는 끝까지로 설정했기 떄문) j는 i 다음부터 N까지 설정
            stack.append(nums[i] * nums[j]) # 모든 곱셈값을 stack에 저장

    for val in stack:       # 곱셈 값을 순회
        tmp = val           # 곱셈 값을 지정하고
        prev = 10           # 10으로 나눈 값으로 단조를 구하려고 하는데 나눈 값은 오른쪽 부터 세기 떄문에 초기값을 10으로 설정
        while tmp > 0:      # tmp가 0이나 작아질 때 까지 반복
            a = tmp % 10    # tmp를 10으로 나눈 나머지(마지막수)
            if a > prev:    # 전에 수(초기값은 10) 와 비교했을때 나머지가 전에 수 보다 크면 종료
                break
            prev = a        # 이전 수를 a로 지정
            tmp //= 10      # 몫을 tmp에 다시 지정하고 반복
        else:
            if val > max_num:   # val이 순회를 다했을 때 max_num 보다 크면
                max_num = val  # max_num의 값에 val을 할당


    print(f'#{tc} {max_num}')