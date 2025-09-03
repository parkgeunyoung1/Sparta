T = int(input())                 # 첫째줄 T 할당
for tc in range(1, T+1):         # tc 1~T번 반복
    N = int(input())             # 숫자 N 할당
    a = 0                        # 초기 지수 할당
    b = 0
    c = 0
    d = 0
    e = 0

    while N != 1:           # N이 1이 될때 까지 반복
        if N % 2 == 0:      # N이 2로 나누어 떨어지면(나머지가 0이면)
            a += 1          # a는 +1
            N = N // 2      # N은  2로 나눈 몫으로 다시 반복
        else:
            break
    while N != 1:           # 위와 똑같은 순환을 3, 5, 7, 11 로 반복
        if N % 3 == 0:
            b += 1
            N = N // 3
        else:
            break
    while N != 1:
        if N % 5 == 0:
            c += 1
            N = N // 5
        else:
            break

    while N != 1:
        if N % 7 == 0:
            d += 1
            N = N // 7
        else:
            break

    while N != 1:
        if N % 11 == 0:
            e += 1
            N = N // 11
        else:
            break


    print(f'#{tc} {a} {b} {c} {d} {e}')