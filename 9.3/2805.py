T = int(input())                 # 첫째줄 T 할당
for tc in range(1, T+1):         # tc 1~T번 반복
    N = int(input())            # N 할당
    farm = [list(map(int, input()))for _ in range(N)]   # farm 리스트 생성
    count = 0                      # 초기 값
    mid = N//2                     # 가운데 번호
    for i in range(N):             # 0~ N-1 까지 순회

        # 가운데 번호보다 행의 번호가 작거나 같을때는 행이 내려올수록 양옆으로 한칸씩 증가한다.
        # 가운데 번호보다 행의 번호가 클때는 행이 끝으로 갈수록 한칸씩 줄어든다.
        if i <= mid:
            s = i
        else:
            s = N - 1 - i
        for j in range(mid-s, mid+s+1):  # 행의번호가 i 일때 농작물 수확의 범위

            count += farm[i][j]     # 행의 번호가 i 일때 총합
                                    # 모든 행 순회
    print(f'#{tc} {count}')