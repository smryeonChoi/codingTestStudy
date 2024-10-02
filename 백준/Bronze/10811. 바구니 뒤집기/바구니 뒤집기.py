n,m = map(int,input().split())
bags = [i for i in range(1,n+1)]
for k in range(m) :
    i,j = map(int,input().split())
    temp = bags[i-1:j] 
    temp.reverse()
    bags[i-1:j] = temp
for q in range(n) :
    print(bags[q],end = ' ')