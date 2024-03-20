the_loai = input("Chọn thể loại phim (1-5): ")
thoi_gian = input("Chọn thời gian xem phim (sáng, trưa, chiều, tối): ")
if the_loai ==  'hành động'or the_loai == 'hài hước':
    if thoi_gian == "sáng" or thoi_gian == "trưa" or thoi_gian == "chiều" or thoi_gian == "tối":
        print(f"Thời gian chiếu phim Hành động/Hài hước: {thoi_gian}")
    else:
        print("Không có suất chiếu nào!!")
elif the_loai == 'kinh dị':
    if thoi_gian == "tối":
        print(f"Thời gian chiếu phim Kinh dị: {thoi_gian}.")
    else:
        print("Không có suất chiếu cho phim Kinh dị vào buổi sáng, trưa và chiều.")
elif the_loai == 'tình cảm':
    if thoi_gian == "tối":
        print(f"Thời gian chiếu phim Tình cảm: {thoi_gian}.")
    else:
        print("Không có suất chiếu cho phim Tình cảm vào buổi sáng, trưa và chiều.")
elif the_loai == 'hoạt hình':
    if thoi_gian == "sáng" or thoi_gian == "trưa":
        print(f"Thời gian chiếu phim Hoạt hình: {thoi_gian}.")
    elif thoi_gian == "chiều" or thoi_gian == "tối":
        print("Không có suất chiếu cho phim Hoạt hình vào buổi chiều và tối.")
    else:
        print("không có suất chiếu nào!!.")
else:
    print("Lựa chọn không hợp lệ.")
