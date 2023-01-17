def rpn(rpn_string):

    stack = []
    for char in rpn_string:
        if char not in "+-/*":
            stack.append(int(char))

        else:
            r, l = stack.pop(), stack.pop()

            if char == "*":
                stack.append(l*r)
            elif char == "+":
                stack.append(l+r)
            elif char == "-":
                stack.append(l-r)
            elif char == "/":
                stack.append(int(float(l) / r))
    print(*stack)
    return stack.pop()


