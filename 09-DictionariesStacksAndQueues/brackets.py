import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()
    matching_brackets = {
        ')': '(', 
        '}' : '{', 
        ']':'['
    }

    for char in expression:
        if char in "({[":
            stack.put(char)
        elif char in ')}]':
            if stack.empty():
                return False

            top = stack.get()
            if matching_brackets[char] != top:
                return False
            
    return stack.empty()

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"  

if brackets_ok(expression1):
    print("Expression 1: Brackets are OK")
else:
    print("Expression 1: Brackets are NOT correct")

if brackets_ok(expression2):
    print("Expression 2: Brackets are OK")
else:
    print("Expression 2: Brackets are NOT correct")

if brackets_ok(expression3):
    print("Expression 3: Brackets are OK")
else:
    print("Expression 3: Brackets are NOT correct")