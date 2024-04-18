
so_luong_phan_tu = int(input("Nhập số lượng phần tử trong mảng: "))

mang = [int(input(f"Nhập số nguyên dương thứ {i + 1}: ")) for i in range(so_luong_phan_tu)]

tong_so_chan = 0
tong_so_le = 0

for so in mang:
    if so % 2 == 0:
        tong_so_chan += so
    else:
        tong_so_le += so

print(f"Tổng các số chẵn trong mảng: {tong_so_chan}")
print(f"Tổng các số lẻ trong mảng: {tong_so_le}")
