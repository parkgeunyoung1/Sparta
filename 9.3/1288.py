T = int(input())                 # 첫째줄 T 할당
for tc in range(1, T+1):         # tc 1~T번 반복
    N = int(input())             # 숫자열 N 받아오기
    count = 0                    # 초기 숫자 횟수는 0
    seem = [0] * 10              # 숫자를 봤는지 기록
    k = 0                        # 양을 세는 횟수
    while count < 10:            # 숫자가 10번(무조건 숫자를 다보는 최대횟수) 샐때까지 반복
        k += 1                   # 양 k번째 읽기
        val = k * N              # 양 k번째의 값
        temp = val               # 값을 저장
        while temp > 0:          # 값이 0보다 작거나 같을 때 까지 반복
            num = temp % 10      # 값을 10으로 나눈 나머지
            if seem[num] == 0:   # 나머지 값이 처음으로 나왔을 때 seem에 1로 기록
                seem[num] = 1
                count += 1        # 변경 횟수 기록
                if count == 10:   # seem이 바뀐 횟수가 10이 될때 끝냄
                    break
            temp //= 10          # 값이 10으로 나눈 몫으로 다시 10으로 나눈 나머지값으로 반복

    print(f'#{tc} {val}')

