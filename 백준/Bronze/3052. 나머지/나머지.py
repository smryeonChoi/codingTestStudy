numbers = [int(input()) for i in range(10)]
for i in range(10) :
    numbers[i] = numbers[i] % 42
print(len(list(set(numbers))))