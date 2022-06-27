# 여러개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 입력 : 행 개수 N, 열 개수 M (1 <= N, M <= 100)
#       각 카드에 적힌 숫자가 주어짐 (1 ~ 10,000)
# 출력 : 게임 룰에 맞게 선택한 카드에 적힌 숫자 출력

n, m = map(int, input().split())

result = 0

# 행이 n개 이므로 n번 만큼 반복하여 입력 받아야함
for i in range(n) :
    # 한 행씩 입력
    rowValues = list(map(int, input().split()))
    # 저장된 결과값이 행의 최소값 보다 작으면 행의 최소값 입력
    result = min(rowValues) if result < min(rowValues) else result

# 출력
print(result)

# 핵심 : min() 함수를 이용하여 코드 길이 줄이기