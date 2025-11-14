import heapq
# jobs : 요청 시점, 소요 시간
# 우선순위 : 소요 시간 짧 -> 요청 시각 빠른 것
def solution(jobs) :
    time = 0 # 현재 시간
    total_time = 0 # 작업 완료될 때까지 걸린 시간들의 합
    limit = -1 # 이전 작업까지 처리하는데 걸린 시간
    cnt = 0 # 처리된 작업 수
    heap = []
    while cnt < len(jobs) : # 모든 작업을 처리할 때까지 반복
        for job in jobs : # 모든 작업을 순회하며
            s,l = job # 작업 요청 시점, 작업 소요 시간
            if limit < s <= time :
                heapq.heappush(heap,[l,s])
        if heap :
            l,s = heapq.heappop(heap) # 우선순위 큐에서 소요시간이 가장 적은 것을 pop
            limit = time
            time += l
            total_time += time - s
            cnt += 1
        else :
            time += 1 # 작업이 없는 경우이므로, 현재 시간을 1초씩 증가 
    return total_time // cnt