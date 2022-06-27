# N에서 1을 빼는 경우와, N을 K로 나누는 방법 두 가지를 활용하여 1을 만드는 최소 횟수를 구하는 알고리즘

N, K = map(int, input().split())

count = 0

while N != 1 :
    if N % K == 0 :
        N = N/K
    else :
        N -= 1

    count += 1

print(count)

# 도서 모범 답안

n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)