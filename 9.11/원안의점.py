T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0              # 초기 갯수
    for x in range(-N, N+1):    # x는 -N ~ N 까지의 정수
        for y in range(-N, N+1):  # y는 -N ~ N 까지의 정수
            if x**2 + y**2 <= N**2:  # 조건에 만족하는 경우를 구한 후 갯수 증가
                count += 1

    print(f'#{tc} {count}')
