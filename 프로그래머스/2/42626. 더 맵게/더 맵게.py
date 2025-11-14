import heapq

def solution(sco,K) :
    ans = 0
    heapq.heapify(sco)
    while sco[0] < K :
        if len(sco) < 2 : return -1 # 모든 음식의 스코빌 지수 K 이상으로 만들 수 없을 때 1 반환
        heapq.heappush(sco,(heapq.heappop(sco) + 2*(heapq.heappop(sco))))
        ans += 1
    return ans
