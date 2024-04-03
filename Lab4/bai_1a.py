#caua:
total = 0
a = []

while total <= 1000:
    b = int(input("Nhập một số nguyên dương: "))
    if b > 0:
        total += b
        if b % 2 != 0:
            a.append(b)
print("Các số lẻ đã nhập:",a)
