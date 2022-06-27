joinDate = list(map(int, input().split()))
calDate = list(map(int, input().split()))

monthVacation = 0
yearVacation = 0

yearDiff = calDate[0] - joinDate[0]
monthDiff = calDate[1] - joinDate[1]
dayDiff = calDate[2] - joinDate[2]

# 월차 계산
monthVacation = yearDiff * 12
monthVacation += monthDiff

if dayDiff < 0 :
    monthVacation -= 1

if monthVacation > 36 :
    monthVacation = 36

# 연차 계산

# A값 계산
for i in range(0, int(yearDiff)) :
    A = i // 2
    yearVacation += A + 15

if monthDiff < 0 or (monthDiff == 0 and dayDiff < 0) :
    yearVacation -= A + 15

print(yearVacation, monthVacation)

#일한 날짜 계산
days = yearDiff * 360 + monthDiff * 30 + dayDiff

print(f'{days}days')



