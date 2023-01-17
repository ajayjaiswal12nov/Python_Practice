def copy_stack(from_stack, to_stack):
    print(from_stack)
    temp_stack = []
    while from_stack:
        temp_stack.append(from_stack.pop())
    print(temp_stack)
    while temp_stack:
        to_stack.append(temp_stack.pop())
    print(to_stack)