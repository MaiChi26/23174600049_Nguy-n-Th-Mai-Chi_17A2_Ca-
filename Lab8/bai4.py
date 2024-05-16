def sumPdivisors(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    return total

n= int(input("nhập vào một số:"))
result = sumPdivisors(n)
print(f"Tổng các ước số chính của {n} là:", result)
