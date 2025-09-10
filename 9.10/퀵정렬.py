def hoare_partition(left, right):
    mid = (left + right) // 2
    pivot = arr[mid]  # 피벗을 중간 요소로 설정
    arr[left], arr[mid] = arr[mid], arr[left]  # 중간 요소를 왼쪽으로 이동 (필요 시)
    i = left + 1    # i는 비펏 다음 인덱스
    j = right       # j 는 가장 오른쪽 인덱스

    while i <= j:                   # 교차하기 전까지 계속
        while i <= j and arr[i] <= pivot:  # 피벗 이하 값은 왼쪽에 있으면 통과 큰 값을 만나면 멈춤
            i += 1                   # i를 오른쪽으로 이동
        while i <= j and arr[j] >= pivot:  # 피벗 이상 값은 오른쪽에 있으면 통과 작은 값을 만나면 멈춤
            j -= 1                   # j를 왼쪽으로 이동
        if i < j:                    # i가 j보다 왼쪽이면
            arr[i], arr[j] = arr[j], arr[i]  # 왼쪽의 큰 값과 오른쪽 작은 값을 교환

    arr[left], arr[j] = arr[j], arr[left]   # 피벗을 j 와 교환
    return j


def quick_sort(left, right):
    if left < right:            
        pivot = hoare_partition(left, right)  # 피벗기준으로 분리하고 피벗 위치 받기
        quick_sort(left, pivot - 1)  # 분리한 부분도 재귀함수
        quick_sort(pivot + 1, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{tc} {arr[N//2]}')
