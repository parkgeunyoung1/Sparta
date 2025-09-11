T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # 기차가 충돌하는 시간
    collision_time = D / (A + B)
    # 파리가 날라다닌 시간 = 기차가 충돌하는 시간
    # 파리가 날라간 거리
    distance_fly = collision_time * F

    print(f'#{tc} {distance_fly}')
