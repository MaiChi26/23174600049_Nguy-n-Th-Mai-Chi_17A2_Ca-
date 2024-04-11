chuoi= input("nhập vào một chuỗi:")
so = ""
for i in chuoi:
    if i.isdigit():
        so+=i
if so:
    n = int(so)
    if n<= 1:
        check= False
    else:
        check = True
        for j in range(2,n):
            if n% j ==0:
                check = False
                break
        if check == True:
            print(f"{n} là số nguyên tố")
            n+=1
        else:
            print(f"{n} không phải là số nguyên tố")
else:
    print("chuỗi không chứa bất kì số nào.")