def merge(left, right):
    global cnt
    if left[-1] > right[-1]:   # 왼쪽부분 마지막 원소가 오른쪽 부분 마지막 원소보다 크면 1증가
        cnt += 1
    result = [0] * (len(left) + len(right))  # 합쳐질 리스트 생성
    l = r = 0   # 초기 왼쪽, 오른쪽 리스트 인덱스

    while l < len(left) and r < len(right):  # 왼쪽, 오른쪽 리스트에 값이 남아있을 때 까지 반복
        if left[l] < right[r]:               # 두 리스트의 현재 원소를 비교해서 더 작은값을 저장
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):                 # 왼쪽 값이 남아 있으면 result에 복사
        result[l + r] = left[l]
        l += 1

    while r < len(right):              # 오른쪽 값이 남아있으면 result에 복사
        result[l + r] = right[r]
        r += 1

    return result               # 병합된 result를 반환

def merge_sort(L):             # 병합 정렬하는 재귀함수 생성
    if len(L) == 1:             # 길이가 1이면 반환
        return L

    mid = len(L) // 2            # 리스트를 반으로 분할
    left = L[:mid]
    right = L[mid:]
    left_list = merge_sort(left)   # 분할된 리스트를 정렬
    right_list = merge_sort(right)

    merged_list = merge(left_list, right_list) # 정렬된 두 리스트를 병합
    return merged_list


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    sorted_L = merge_sort(L)

    print(f'{tc} {sorted_L[N // 2]} {cnt}')
