T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    N = int(input())      # 16진수 문자열 길이
    num = input().strip()  # 16진수 문자열

    result = 0
    for ch in num:
        # int(ch, 16) → 한 자리 16진수를 10진수로 변환
        result += int(ch, 16)

    print(f"#{tc} {result}")
