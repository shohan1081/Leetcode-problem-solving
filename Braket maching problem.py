def is_paren_balanced(paren_string):
    stack = []
    i = 0
    opens = {')': '(', '}': '{', ']': '['}
    bal = True

    while i < len(paren_string) and bal == True:
        paren = paren_string[i]
        if paren in '([{':
            stack.append(paren)
        else:
            if not stack:
                bal = False
                return bal
            else:
                if stack[-1] != opens[paren]:
                    bal = False
                    return bal
                else:
                    stack.pop()
        i += 1
    
    if stack:
        bal = False
    
    return bal
print(is_paren_balanced('(())))'))
               