N,M = map(int,input().split())
bag = [0] * N
for i in range(N) :
    bag[i] = (i+1)
for _ in range(M) :
    i,j = map(int,input().split())
    bag[i-1],bag[j-1] = bag[j-1],bag[i-1] # idx이므로 - 1


for i in range(N) :
    print(bag[i],end = ' ')