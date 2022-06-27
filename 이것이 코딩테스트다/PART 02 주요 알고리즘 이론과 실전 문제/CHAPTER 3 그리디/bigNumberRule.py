""" 내 답안 """
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

firstBig, secondBig = 0, 0
sum = 0
count = 0

# 첫 번째로 큰 수 찾기
for value in data:
    if value >= firstBig:
        secondBig = firstBig
        firstBig = value
    if value > secondBig and value < firstBig:
        secondBig = value

for _ in range(M):
    count += 1
    if count > K:
        count = 0
        sum += secondBig
    else:
        sum += firstBig

print(sum)

""" 모범 답안 """

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

sum = 0
data.sort()

first = data[n-1]
second = data[n-2]

while True:
    for _ in range(k):
        sum += first
        m -= 1
        if m == 0:
            break
    sum += second
    m -= 1
    if m == 0:
        break

print(sum)

""" 수열을 이용한 답안 """

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬 후 제일 큰 수와 작은 수 선정
data.sort()
first = data[n-1]
second = data[n-2]

# 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)