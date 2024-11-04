# 遞迴
def fib_Rec(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = fib_Rec(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# 迭代
def fib_Iter(n):
    arr = [0, 1]
    first, second = 0, 1
    for _ in range(2, n + 1):
        first, second = second, first + second
        arr.append(second)
    return arr
        

# 產生器
def fib_Gen(n): 
    first, second = 0, 1
    for _ in range(n + 1):
        yield first
        first, second = second, first + second

def fib(n, func):
    result = func(n)
    return result

def main():
    n = int(input("請輸入一個整數: "))
    rec = fib(n, fib_Rec)
    ite = fib(n, fib_Iter)
    gen = fib(n, fib_Gen)

    print("遞迴方式: ")
    print(f"F({n}) = {', '.join(map(str, rec))}")
    print("迭代方式: ")
    print(f"F({n}) = {', '.join(map(str, list(iter(ite))))}")
    print("產生器方式: ")
    print(f"F({n}) = {', '.join(map(str, gen))}")

if __name__ == "__main__":
    main()