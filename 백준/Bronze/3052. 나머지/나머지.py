numbers = []
rest = []
for i in range(10) :
    num = int(input())
    numbers.append(num)
for i in numbers :
    a = i % 42
    rest.append(a)
print(len(list(set(rest))))
