print("Danh sách các thể loại phim:")
print("1. Hành động")
print("2. Kinh dị")
print("3. Tình cảm")
print("4. Hài hước")
print("5. Hoạt hình")
the_loai = int(input("Chọn thể loại phim (1-5): "))
thoi_gian = input("Chọn thời gian xem phim (sáng, trưa, chiều, tối): ")
if the_loai == 1 or the_loai == 4:
    if thoi_gian == "sáng" or thoi_gian == "trưa" or thoi_gian == "chiều" or thoi_gian == "tối":
        print(f"Thời gian chiếu phim Hành động/Hài hước: {thoi_gian}")
    else:
        print("Thời gian không hợp lệ.")
elif the_loai == 2:
    if thoi_gian == "tối":
        print(f"Thời gian chiếu phim Kinh dị: {thoi_gian}.")
    else:
        print("Không có suất chiếu cho phim Kinh dị vào buổi sáng, trưa và chiều.")
elif the_loai == 3:
    if thoi_gian == "tối":
        print(f"Thời gian chiếu phim Tình cảm: {thoi_gian}.")
    else:
        print("Không có suất chiếu cho phim Tình cảm vào buổi sáng, trưa và chiều.")
elif the_loai == 5:
    if thoi_gian == "sáng" or thoi_gian == "trưa":
        print(f"Thời gian chiếu phim Hoạt hình: {thoi_gian}.")
    elif thoi_gian == "chiều" or thoi_gian == "tối":
        print("Không có suất chiếu cho phim Hoạt hình vào buổi chiều và tối.")
    else:
        print("Thời gian không hợp lệ.")
else:
    print("Lựa chọn không hợp lệ.")