m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        nhap_phan_tu = int(input(f"Nhập phần tử ở hàng {i+1} cột {j+1}: "))
        hang.append(nhap_phan_tu)
    ma_tran.append(hang)
tong = 0
for hang in ma_tran:
    tong += sum(hang)
tich = 1
for hang in ma_tran:
    for phan_tu in hang:
        tich *= phan_tu
ma_tran_chuyen_vi = []
for i in range(n):
    hang_chuyen_vi = []
    for j in range(m):
        hang_chuyen_vi.append(ma_tran[j][i])
    ma_tran_chuyen_vi.append(hang_chuyen_vi)
print("Ma trận đã nhập:")
for hang in ma_tran:
    print(hang)
print("Tổng các phần tử trong ma trận:", tong)
print("Tích các phần tử trong ma trận:", tich)
print("Ma trận chuyển vị:")
for hang in ma_tran_chuyen_vi:
    print(hang)
