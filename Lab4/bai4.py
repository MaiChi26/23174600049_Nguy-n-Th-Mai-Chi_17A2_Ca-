n = int(input("Nhập số nguyên n ( n > 10): "))
if n <= 10:
    print("Số không hợp lệ.")
else:
    a = 0 
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
    while a < n:
        S1 += 6**a 
        S2 += 1/(3**(2*a+1))
        S3 += (-1)**a*a**2
        S4 += a*(a + 1)*(a + 2 )        
        a += 1 
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)