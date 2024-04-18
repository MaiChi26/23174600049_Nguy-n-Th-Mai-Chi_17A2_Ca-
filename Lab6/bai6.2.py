n = int(input("Nhập kích thước ma trận vuông: "))
ma_tran_vuong = []
for i in range(n):
    hang = []
    for j in range(n):
        phan_tu = float(input(f"Nhập phần tử [{i}][{j}]: "))
        hang.append(phan_tu)
    ma_tran_vuong.append(hang)
ma_tran_don_vi = []
for i in range(n):
    hang = [0] * n
    hang[i] = 1
    ma_tran_don_vi.append(hang)
ma_tran_ghiep = []
for i in range(n):
    hang_ghiep = ma_tran_vuong[i] + ma_tran_don_vi[i]
    ma_tran_ghiep.append(hang_ghiep)
for i in range(n):
    he_so_chia = ma_tran_ghiep[i][i]
    for j in range(2*n):
        ma_tran_ghiep[i][j] /= he_so_chia

    for k in range(n):
        if k != i:
            he_so_nhan = ma_tran_ghiep[k][i]
            for j in range(2*n):
                ma_tran_ghiep[k][j] -= he_so_nhan * ma_tran_ghiep[i][j]
ma_tran_nghich_dao = []
for i in range(n):
    hang_nghich_dao = []
    for j in range(n, 2*n):
        hang_nghich_dao.append(ma_tran_ghiep[i][j])
    ma_tran_nghich_dao.append(hang_nghich_dao)
print("Ma trận nghịch đảo:")
for hang in ma_tran_nghich_dao:
    print(hang)