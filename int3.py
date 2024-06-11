def fibonacci(num):
    sequence = []
    a, b = 0, 1
    while len(sequence) < num:
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))
