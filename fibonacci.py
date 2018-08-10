def fibonacci_generator(number):
    yield 0
    yield 1
    a, b = 0, 1
    while (a < number):
        yield a + b
        a, b = b, a + b

for num in fibonacci_generator(1000):
    print(num)

print(list(fibonacci_generator(1000)))

def fibonacci(n):
    fn = [0, 1,]
    for i in range(2, n):
        fn.append(fn[i-1] + fn[i-2])
    return fn
print(fibonacci(19))
