def solution(balls,share) :
    up = 1
    for i in range(balls-share+1,balls+1) :
        up = up * i
    down = 1
    for i in range(1,share+1) :
        down = down * i
    return int(up/down)