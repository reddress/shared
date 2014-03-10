def checkio(expr):
    left_brackets = "([{"
    bracket_pair =  {")": "(", "]": "[", "}": "{"}
    stack = []
    for c in expr:
        if c in left_brackets:   # run into opening bracket
            stack.append(c)
        if c in bracket_pair:    # run into closing bracket
            if len(stack) == 0:
                return False     # closing bracket without opening one
            elif stack[-1] == bracket_pair[c]:  # last opening bracket matches
                stack.pop()
            elif stack[-1] != bracket_pair[c]:
                return False
    print(stack)
    return len(stack) == 0

checkio("(((([[[{{{3}}}]]]]))))")
checkio("(((([]])))")
