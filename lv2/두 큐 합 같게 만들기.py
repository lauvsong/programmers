def solution(queue1, queue2):
    answer = 0
    
    arr = queue1 + queue2
    q1_sum = sum(queue1)
    target = (q1_sum + sum(queue2)) // 2
    
    n = len(arr)
    
    left = 0
    right = len(queue1) - 1
    
    while q1_sum != target:
        if answer == 2 * n: 
            return -1
        
        if q1_sum < target:
            right += 1
            if right == len(arr):
                right = 0
            q1_sum += arr[right]
        else:
            q1_sum -= arr[left]
            left += 1
            if left == len(arr):
                left = 0
        answer += 1
    
    return answer

    
"""
# 문제
각 큐의 원소 합이 같게 하기 위해 필요한 작업의 '최소' 횟수 (불가능할 시 -1)

# 그리디
sum(a) < sum(b) 일 시
- b에서 a에 pop 해줌.

# 투포인터
1. a < b 일 시
right += 1

2. a > b 일 시
left += 1

"""