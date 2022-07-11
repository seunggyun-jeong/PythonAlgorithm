# 재귀(Recursion)의 깊이를 초과하면 다음과 같은 오류가 발생 -> RecursionError: maximum recursion depth exceeded while calling a Python object
# 파이썬 인터프리터는 호출 횟수 제한이 있음

def recursive_function():
    print("재귀함수를 호출합니다.")
    recursive_function()

recursive_function()