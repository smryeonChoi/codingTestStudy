n =  int(input())
scores = list(map(int,input().split()))
best = max(scores)
for i in range(n) :
    scores[i] = (scores[i]/best)*100
average = sum(scores)/n
print(average)