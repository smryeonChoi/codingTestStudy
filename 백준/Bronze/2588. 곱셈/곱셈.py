x = []
a = int(input())
b = int(input())
while b > 0 :
    x.append(b%10)
    b = b // 10
print(a*x[0])
print(a*x[1])
print(a*x[2])
print(a*x[0]+ a*x[1]*10 + a*x[2]*100)