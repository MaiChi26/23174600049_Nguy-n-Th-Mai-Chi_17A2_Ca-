
kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Giả sử khách hàng mua các mặt hàng sau, với số lượng
mua_hang = {}
print("Nhập số lượng mua cho từng mặt hàng (nhập 0 nếu không mua):")
for mat_hang in kho:
    so_luong = int(input(f"Số lượng {mat_hang}: "))
    if so_luong > 0:
        if so_luong <= kho[mat_hang]:
            mua_hang[mat_hang] = so_luong
        else:
            print(f"Không đủ hàng trong kho cho {mat_hang}. Hiện chỉ có {kho[mat_hang]}.")

# Tính hóa đơn
tong_tien = 0
print("Hóa đơn mua hàng:")
print("Mặt hàng\tSố lượng\tĐơn giá\tSố tiền")
for mat_hang, so_luong in mua_hang.items():
    if mat_hang in kho and so_luong <= kho[mat_hang]:
        don_gia = gia_tien[mat_hang]
        so_tien = so_luong * don_gia
        tong_tien += so_tien
        # Cập nhật kho hàng
        kho[mat_hang] -= so_luong
        # In thông tin mặt hàng
        print(f"{mat_hang}\t\t{so_luong}\t\t{don_gia}\t{so_tien}")
    else:
        print(f"{mat_hang} không đủ hàng hoặc không tồn tại trong kho!")

# In tổng số tiền của hóa đơn
print("Tổng số tiền cần thanh toán: ", tong_tien)

# In lại số lượng hàng trong kho
print("\nSố lượng hàng trong kho sau khi mua:")
for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong}")
