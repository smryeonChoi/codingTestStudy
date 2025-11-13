from collections import deque
def solution(progresses,speeds) :
    time = [(100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else ((100 - progresses[i]) // speeds[i]) + 1 for i in range(len(progresses))]
    time = deque(time)
    ans = []
    while time :
        temp = time.popleft()
        count = 1
        while time and temp >= time[0] :
            time.popleft()
            count += 1
        ans.append(count)
    return ans