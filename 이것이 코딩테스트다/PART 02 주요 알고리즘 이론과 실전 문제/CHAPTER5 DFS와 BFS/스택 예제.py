# 파이썬에서 기본적으로 stack을 구현할 수 있는 append와 pop 메서드를 제공해줌
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])