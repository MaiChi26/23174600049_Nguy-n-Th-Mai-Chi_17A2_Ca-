
day_so = list(map(int, input("Nhập vào dãy số, cách nhau bởi dấu cách: ").split()))
la_cap_so_cong = True

if len(day_so) >= 3:
    khoang_cach = day_so[1] - day_so[0]
    for i in range(2, len(day_so)):
        if day_so[i] - day_so[i - 1] != khoang_cach:
            la_cap_so_cong = False
            break
else:
    la_cap_so_cong = False  

if la_cap_so_cong:
    print("Dãy số này tạo thành cấp số cộng:", day_so)
else:
    print("Dãy số này không tạo thành cấp số cộng.")
