a, b, c = map(int,input("Nhập các số a,b,c: ").split())
# Kiểm tra và tìm số lớn thứ hai
if a >= b and a >= c:
    if b >= c:
        so_lon_thu_2 = b
    else:
       so_lon_thu_2 = c
elif b >= a and b >= c:
    if a >= c:
        so_lon_thu_2 = a
    else:
        so_lon_thu_2 = c
else:
    if a >= b:
        so_lon_thu_2 = a
    else:
        so_lon_thu_2 = b
print("Số lớn thứ hai là:", so_lon_thu_2)