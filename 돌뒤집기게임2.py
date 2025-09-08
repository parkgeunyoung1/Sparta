T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))   # N, M 값 설정
    arr = list(map(int, input().split()))    # 초기 돌 형태

    # M번 돌 뒤집기 수행
    for _ in range(M):
        i, j = list(map(int, input().split()))

        m = i - 1 # 중심 좌표 먼저 구하기  (index)
        for step in range(1, j+1):
            # m-step 또는 m+step이 주어진 범위를 벗어난 경우
            # => 돌 뒤집기 불가 => break 멈춤
            if m-step < 0 or m+step >= N:
                break

            if arr[m-step] == arr[m+step]:     # 마주보는 돌의 색이 같으면 뒤집기
                arr[m-step] = 1 - arr[m-step]
                arr[m+step] = 1 - arr[m+step]


        #[1, 1, 1, 1, 0]
        #1 1 1 1 1 0
    # arr에 리스트안에 있는 요소만 꺼내서 출력
    # 안에 요소를 문자열로 변환 후  ' ',join으로 변환

    arr = [str(num) for num in arr]
    print(f"#{tc} {' '.join(arr)}")