chieu_cao = float(input("nhập chiều cao:"))
can_nang = float(input("nhập cân nặng:"))
BMI = can_nang/((chieu_cao)**2)
print("chỉ số BMI là:",BMI)
if BMI<18.5:
    print("chỉ số BMI hiển thị 'Gầy'!!")
elif 18.5 < BMI < 24.9:
    print("chỉ số BMI hiển thị 'Bình thường'!!")
elif 25.0 < BMI < 29.9:
    print("chỉ số BMI hiển thị 'Hơi béo'!!") 
elif BMI> 30.0:
    print("chỉ số BMI hiển thị 'Gầy'!!")
else:
    print("nhập không hợp lệ!!!!!") 