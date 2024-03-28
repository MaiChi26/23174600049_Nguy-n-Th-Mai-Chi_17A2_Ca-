print("Chuỗi Fibonacci mà số cuối trong chuỗi nhỏ hơn 100 là: ", end = " ")
a = 0 
b = 0
c = 1 
for i in range(0, 100):
    b = a + b
    a = c 
    c = b 
    if c < 100: 
        print(c, end = " ")
print()