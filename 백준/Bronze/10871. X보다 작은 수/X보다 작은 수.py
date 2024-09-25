N, X = map(int, input().split())
N_List = list(map(int, input().split()))
for i in range(N) :
    if N_List[i] < X :
        print(N_List[i], end=" ")