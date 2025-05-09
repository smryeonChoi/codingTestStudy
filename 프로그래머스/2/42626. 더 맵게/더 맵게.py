# 리스트의 sort 사용하게 되면 매번 정렬 시행 -> 시간복잡도 증가
# heapq를 사용하게 되면 heapq[0]이 항상 가장 작은 값

import heapq
def solution(scoville,K) :
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K:
        if len(scoville) < 2 : return -1
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        answer += 1
    return answer
'''
import heapq
def solution(sco,K) :
    heapq.heapify(sco) # 리스트 sco 자체가 힙 구조로 변환
    ans = 0
    while sco[0] < K :  # 힙 구조이기 때문에 항상 가장 작은 값 보장
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에 -1
        if len(sco) < 2 : return -1
        heapq.heappush(sco,heapq.heappop(sco) + heapq.heappop(sco) * 2)
        ans += 1
    return ans
'''