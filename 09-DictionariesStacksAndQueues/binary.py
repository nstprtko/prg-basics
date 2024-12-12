import queue # import queue module

def decimal_to_bin(number):
    stack = queue.LifoQueue() # say that this value is a stacl LifoQueue

    while number > 0: # as
        remainder = number % 2
        stack.put(remainder)
        number //=2

    binary = ""
    while not stack.empty():
        binary += str(stack.get())

    return binary

number = 18

binary_result = decimal_to_bin(number)

print(binary_result)