n=int(input("nhập vào một số nguyên:"))
#câua:
tong = 0
if n<=0:
    print("yêu cầu nhập lại!!")
else:
    for i in range(1,n+1):
        tong+=i
print("biểu thức S1 = ",tong)

#câub:
tong = 0
if n<=0:
    print("yêu cầu nhập lại!!")
else:
    for i in range(1,n+1):
        tong+= 1/i
print("biểu thức S2 = ",tong)

#câuc:
import math
tong = 1
if n<=0:
    print("yêu cầu nhập lại!!")
else:
    for i in range(1,n+1):
        tong = tong + 1/(math.sqrt(2*i))
print("biểu thức S3 = ",tong)

#câud:
sum = 0
if n<0:
    print("yêu cầu nhập lại!!")
else:
    for i in range(1,n+1):
        sum+= ((-1)**(i+1))/i
print("biểu thức S4 = ",sum)

