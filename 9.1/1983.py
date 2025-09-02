T = int(input())
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]                      # T 삽입
for tc in range(1, T+1):                 # tc 생성
    N, K = map(int,input().split())       # N, K 값 부여      
    scores = []              # (학생, 점수) 리스트를 얻기 위해 빈 리스트를 부여
    for i in range(1, N + 1):
        mid, fin, hw = map(int, input().split())
        total = mid * 0.35 + fin * 0.45 + hw * 0.20
        scores.append((i, total))

    # --- 선택 정렬로 내림차순 정렬 ---
    for i in range(N-1):
        max_idx = i
        for j in range(i+1, N):
            if scores[j][1] > scores[max_idx][1]:  # 더 큰 점수 찾기
                max_idx = j
        scores[i], scores[max_idx] = scores[max_idx], scores[i]

    # --- K번째 학생 순위 찾기 ---
    target_total = 0
    for stu, total in scores:
        if stu == K:               #  K번째 학생 점수 찾기
            target_total = total
            break

    rank_index = 0
    for _, total in scores:                  # K번째 학생 점수보다 큰 학생들의 수를 세어 순위 찾기
        if total > target_total:
            rank_index += 1
    # --- 학점 계산 ---
    bucket = N // 10
    grade_idx = rank_index // bucket

    print(f"#{t} {grades[grade_idx]}")

