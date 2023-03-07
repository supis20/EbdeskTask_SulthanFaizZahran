def Task1_Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Task1_Fibonacci(n-1) + Task1_Fibonacci(n-2)

n = int(input("Input berapa banyak angka yang ingin dihasilkan dalam deret Fibonacci: "))

if n <= 0:
    print("Input angka lebih dari 1")
else:
    print("Deret Fibonacci:")
    for i in range(n):
        print(Task1_Fibonacci(i), end=" ")