def tinh_giai_thua(n):
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def permutation(n, r):
    if r > n:
        return 0
    return tinh_giai_thua(n) / tinh_giai_thua(n - r)
def combination(n, r):
    if r > n:
        return 0
    return tinh_giai_thua(n) / (tinh_giai_thua(r) * tinh_giai_thua(n - r))

n = int(input("nhập vào một số:"))
r = int(input("nhập vào một số:"))
# Tính số hoán vị
perm = permutation(n, r)
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là: {perm}")

# Tính số tổ hợp
comb = combination(n, r)
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: {comb}")
