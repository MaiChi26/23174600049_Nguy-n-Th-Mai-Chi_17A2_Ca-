#bài3:
p = 10000
r = 0.06
n1 = 5
n2 = 10
amount_after_5_years = p*(1+r)**n1
amount_after_10_years = p*(1+r)**n2
growth_rate = (amount_after_10_years - amount_after_5_years)/p
print("số tiền có được sau 5 năm: {: 2f}".format(amount_after_5_years))
print("số tiền có được sau 10 năm: {: 2f}".format(amount_after_10_years))
print("tỷ lệ tăng trưởng: {: 2f}".format(growth_rate))

