n = int(input("Nhập số Fibonacci đầu tiên: "))
fibonacci = [0, 1]
for i in range(2, n):
    a = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(a)

print("Dãy Fibonacci đầu tiên là:", fibonacci)

tong = sum(fibonacci)
list_1 = []
for so in range(2, tong):
    neu_so = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            neu_so = False
            break
    if neu_so:
        list_1.append(so)

print("Danh sách các số nguyên tố nhỏ hơn tổng của dãy Fibonacci là:", list_1)