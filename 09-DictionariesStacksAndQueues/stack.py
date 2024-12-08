stack = []

stack.append(2)
stack.append(3)
stack.append(7)
stack.append(4)
stack.append(1)
stack.append(9)
stack.append(8)

last_two_sum = stack.pop() + stack.pop()
print(last_two_sum)

remaining_sum = 0
while stack :
    remaining_sum += stack.pop()

print(remaining_sum)