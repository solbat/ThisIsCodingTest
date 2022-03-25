# 5-1.py 스택 예제

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
a1 = stack.pop()
stack.append(1)
stack.append(4)
a2 = stack.pop()

print(stack)
print(a1, a2)
print(stack[::-1])