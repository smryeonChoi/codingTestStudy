from collections import deque
def solution(priorities,location) :
    order = 0
    queue = deque([i,p] for i,p in enumerate(priorities))
    
    while queue :
        index,priority = queue.popleft()
        if any(priority < other_priority for _,other_priority in queue) :
            queue.append([index,priority])
        else :
            order += 1
            if index == location :
                return order
    