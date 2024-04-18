# Nhập dãy số từ bàn phím
day_so = list(map(float, input("Nhập vào dãy số, cách nhau bởi dấu cách: ").split()))

# Tìm số lớn nhất và số nhỏ nhất trong dãy số
so_lon_nhat = max(day_so)
so_nho_nhat = min(day_so)

print("Số lớn nhất trong dãy số là:", so_lon_nhat)
print("Số nhỏ nhất trong dãy số là:", so_nho_nhat)
