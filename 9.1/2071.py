T = int(input())               
for tc in range(1, T+1):    
    num = list(map(int, input().split())) # 숫자열 리스트 할당
    num_sum = 0  # 초기 숫자합
    count = 0    # 숫자 갯수
    for i in num:      # 숫자열 순회
        num_sum += i     # 숫자 더하기
        count += 1       # 숫자 갯수 새기
    result = round(num_sum / count)   # 반올림
 
    print(f'#{tc} {result}')
