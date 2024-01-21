while True:
    string = input()
    if string == '.':
        break
    stack = []
    answer = "yes"

    for char in list(string):
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']':
            if not stack:
                answer = "no"
            elif stack[-1] == '[':
                stack.pop()
            else:
                answer = "no"
        elif char == ')':
            if not stack:
                answer = "no"
            elif stack[-1] == '(':
                stack.pop()
            else:
                answer = "no"
    if len(stack) > 0:
        answer = "no"
    print(answer)
