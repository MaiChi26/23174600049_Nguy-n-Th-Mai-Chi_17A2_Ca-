#Ý1:
def loc_so_le(danh_sach):
    return list(filter(lambda x: x % 2 != 0, danh_sach))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lọc các số lẻ từ danh sách bằng cách sử dụng hàm filter:")
print(loc_so_le(danh_sach))


# Ý2:
def loc_so_chan(danh_sach):
    return list(filter(lambda x: x % 2 == 0, danh_sach))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lọc các số chẵn từ danh sách bằng cách sử dụng hàm filter:")
print(loc_so_chan(danh_sach))


#Ý3:
def lap_phuong_danh_sach(danh_sach):
    return list(map(lambda x: x ** 3, danh_sach))

danh_sach = [1, 2, 3, 4, 5]
print("Sử dụng hàm map để tạo danh sách các lập phương từ danh sách ban đầu:")
print(lap_phuong_danh_sach(danh_sach))



#Ý4:
def loc_va_map_lap_phuong_so_chan(danh_sach):
    return list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, danh_sach)))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sử dụng hàm map và filter để tạo danh sách lập phương của các số chẵn từ danh sách ban đầu:")
print(loc_va_map_lap_phuong_so_chan(danh_sach))


#Ý5:
def loc_va_map_binh_phuong_so_le(danh_sach):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, danh_sach)))

danh_sach = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sử dụng hàm map và filter để tạo danh sách bình phương của các số lẻ từ danh sách ban đầu:")
print(loc_va_map_binh_phuong_so_le(danh_sach))

