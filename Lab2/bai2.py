n = int(input("Nhập vào số nguyên: "))
chu_so_hang_nghin = n// 1000
if chu_so_hang_nghin == 0:
    print("Số không có chữ số hàng nghìn")
elif 0 < chu_so_hang_nghin <= 9:
    print("Chữ số hàng nghìn là:",chu_so_hang_nghin)
else:
    phan_du = chu_so_hang_nghin % 100
    if phan_du == 0:
        print("Chữ số hàng nghìn là:",0)
    else:
        print("Chữ số hàng nghìn là:",phan_du)