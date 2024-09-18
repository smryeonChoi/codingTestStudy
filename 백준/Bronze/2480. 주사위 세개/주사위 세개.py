numbers = list(map(int,input().split()))
numbers.sort(reverse=True)
a,b,c = numbers

if a == b and b == c :
    money = 10000 + (1000*a)
elif (a==b and b!=c) or (a!=b and b==c) :
    money = 1000 + (100*b)
else :
    money = 100*a
print(money)