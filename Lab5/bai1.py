
a = int(input("Nhập một số nguyên dương: "))
if a <= 0:
    so_nhi_phan = "Vui lòng nhập một số nguyên dương"
else:
    so_nhi_phan = ''
    while a > 0:
        phan_con_lai = a % 2
        so_nhi_phan = str(phan_con_lai) + so_nhi_phan
        a = a // 2
print(f"Số nhị phân tương ứng là: {so_nhi_phan}")