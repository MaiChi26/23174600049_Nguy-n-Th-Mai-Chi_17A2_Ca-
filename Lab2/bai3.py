n = int(input("Nhập số nguyên có 3 chữ số: "))

if 99 < n < 1000:
    chu_so_hang_tram = n // 100
    chu_so_hang_chuc = (n // 10) % 10
    chu_so_hang_don_vi = n % 10

    # Đọc chữ số hàng trăm
    if chu_so_hang_tram == 1:
        doc_hang_tram = "One hundred"
    elif chu_so_hang_tram == 2:
        doc_hang_tram = 'Two hundred'
    elif chu_so_hang_tram == 3:
        doc_hang_tram = 'Three hundred'
    elif chu_so_hang_tram == 4:
        doc_hang_tram = 'Four hundred'
    elif chu_so_hang_tram == 5:
        doc_hang_tram = 'Five hundred'
    elif chu_so_hang_tram == 6:
        doc_hang_tram = 'Six hundred'
    elif chu_so_hang_tram == 7:
        doc_hang_tram = 'Seven hundred'
    elif chu_so_hang_tram == 8:
        doc_hang_tram = 'Eight hundred'
    elif chu_so_hang_tram == 9:
        doc_hang_tram = 'Nine hundred'
    elif chu_so_hang_tram == 0:
        print("khoong co so hang tram")
    # Đọc chữ số hàng chục và hàng đơn vị
    if chu_so_hang_chuc == 1:  # Đặc biệt xử lý khi hàng chục là 1
        if chu_so_hang_don_vi == 0:
            doc_hang_chuc = 'ten'
        elif chu_so_hang_don_vi == 1:
            doc_hang_chuc  = 'eleven'
        elif chu_so_hang_don_vi == 2:
            doc_hang_chuc = 'twelve'
        elif chu_so_hang_don_vi == 3:
            doc_hang_chuc = 'thirteen'
        elif chu_so_hang_don_vi == 4:
            doc_hang_chuc = 'fourteen'
        elif chu_so_hang_don_vi == 5:
            doc_hang_chuc = 'fifteen'
        elif chu_so_hang_don_vi == 6:
            doc_hang_chuc = 'sixteen'
        elif chu_so_hang_don_vi == 7:
            doc_hang_chuc = 'seventeen'
        elif chu_so_hang_don_vi == 8:
            doc_hang_chuc = 'eighteen'
        elif chu_so_hang_don_vi == 9:
            doc_hang_chuc = 'nineteen'
        doc_hang_don_vi = '' # Không cần đọc hàng đơn vị nếu đã xử lý từ 11 đến 19
    else:
        if chu_so_hang_chuc == 2:
            doc_hang_chuc = 'twenty'
        elif chu_so_hang_chuc == 3:
            doc_hang_chuc = 'thirty'
        elif chu_so_hang_chuc == 4:
            doc_hang_chuc = 'forty'
        elif chu_so_hang_chuc == 5:
            doc_hang_chuc = 'fifty'
        elif chu_so_hang_chuc == 6:
            doc_hang_chuc = 'sixty'
        elif chu_so_hang_chuc == 7:
            doc_hang_chuc = 'seventy'
        elif chu_so_hang_chuc == 8:
            doc_hang_chuc = 'eighty'
        elif chu_so_hang_chuc == 9:
            doc_hang_chuc = 'ninety'
        elif chu_so_hang_chuc == 0:
            doc_hang_chuc = ''
    if chu_so_hang_don_vi != 0 and chu_so_hang_chuc!=1:  # Đọc hàng đơn vị nếu không phải là trường hợp đặc biệt từ 11 đến 19
        if chu_so_hang_don_vi == 1:
                doc_hang_don_vi = "one"
        elif chu_so_hang_don_vi == 2 :
                doc_hang_don_vi = 'two'
        elif chu_so_hang_don_vi == 3:
                doc_hang_don_vi = 'three'
        elif chu_so_hang_don_vi == 4:
                doc_hang_don_vi = 'four'
        elif chu_so_hang_don_vi == 5:
                doc_hang_don_vi = 'five'
        elif chu_so_hang_don_vi == 6:
                doc_hang_don_vi = 'six'
        elif chu_so_hang_don_vi == 7:
                doc_hang_don_vi = 'seven'
        elif chu_so_hang_don_vi == 8:
                doc_hang_don_vi = 'eight'
        elif chu_so_hang_don_vi == 9:
                doc_hang_don_vi = 'nine'
        else:
            doc_hang_don_vi = ''
    print("Số", n, "đọc là:", doc_hang_tram, doc_hang_chuc, doc_hang_don_vi)
else:
    print("Nhập số không hợp lệ, vui lòng thử lại!!!")