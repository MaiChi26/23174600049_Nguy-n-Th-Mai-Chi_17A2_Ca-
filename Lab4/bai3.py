a = int(input("Nhập vào một số nguyên: "))
count = 0
b = abs(a)  
while b > 0:
    count += 1
    b //= 10 

if a == 0:
    count = 1

print(f"Số {a} có {count} chữ số.")