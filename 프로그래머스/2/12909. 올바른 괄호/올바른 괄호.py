def solution(s) :
    stacks = []
    for i in s :
        if i == '(' :
            stacks.append(i)
        else :
            if stacks == [] :
                return False 
            else :
                stacks.pop() 
    if stacks != [] :
        return False 
    return True