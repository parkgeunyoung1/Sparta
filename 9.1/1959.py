T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 항상 A가 더 짧도록 맞춤.
    if N > M:
        N, M = M, N
        A, B = B, A

    # 슬라이딩하며 최대 합 갱신
    max_sum = None           # 처음 max_sum이 음수가 될수있어서 0대신 None 을 사용
    for s in range(M - N + 1):  # s: B에서의 시작 인덱스
        total = 0
        for i in range(N):
            total += A[i] * B[s + i]
        if (max_sum is None) or (total > max_sum):
            max_sum = total

    print(f"#{tc} {max_sum}")
