from random import randint
import time

# 배열에 10,000개 정수 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 알고리즘
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
selection_sorting_time = end_time - start_time
print("선택 정렬 성능 측정 :", selection_sorting_time)

# 배열 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

# 기본 정렬 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()
basic_sorting_time = end_time - start_time
print("기본 정렬 성능 측정 :", basic_sorting_time)

if basic_sorting_time > selection_sorting_time:
    print("선택 정렬이 시간적으로 이득")
else:
    print("기본 정렬이 시간적으로 이득")



