T = int(input())              # 첫째줄 T 할당
for tc in range(1, T+1):      # tc 1~T번 반복
    N = input().strip()       # 문자열 N 받아오기
    memory = '0'              # memory는 0
    count = 0                 # 초기 수정횟수는 0
    for i in N:               # 문자열 N에서 순회
        if i != memory:       # 문자가 memory가 아니면(1이면)
            count += 1        # 수정횟수 1회 추가
            memory = i        # memory를 i로 (1) 로 바꾸고 다음 문자에 똑같이 순회


# ex) 0010일때 처음순회때 0이여서 넘어가고

    # 3번째 문자인 1이 momory = '0'과 일치하지 않아서
    # 횟수 1회 추가하고 momory = '1' 로 변경 후 실행
    # 그다음 문자인 0 은 momory = '1' 과 다르기 때문에 횟수를 추가하고
    # momory = '0'으로 변경
    # 첫순회 0010, 두번째 0010, 세번째 0001 네번째 0000 (역으로) 총 2번 바뀜
    print(f'#{tc} {count}')