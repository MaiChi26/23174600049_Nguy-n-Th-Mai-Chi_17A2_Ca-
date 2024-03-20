a = int(input("nhập số lượng người đi xem phim:"))
gia_ve = 120000
if a==1:
    tong_tien = gia_ve
elif 2<=a<=4:
    tong_tien = a*gia_ve*(1-0.05)
elif 4<a<=10:
    tong_tien = a*gia_ve*(1-0.1)
else:
    tong_tien = a*gia_ve*(1-0.2)
print("tổng tiền phải trả với {} người là: {} đồng".format(a,tong_tien))
    
