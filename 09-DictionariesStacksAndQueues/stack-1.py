import queue

stack = queue.LifoQueue()

stack.put(1)
stack.put(2)
stack.put(5)

last_two_sum = stack.pop() + stack.pop()
print(last_two_sum)