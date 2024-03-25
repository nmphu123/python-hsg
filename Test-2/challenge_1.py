# Đọc file input
fi = open('cau1.inp')
n = int(fi.read())
fi.close()

# Thuật toán tính tổng
sum = 0
for i in range(1, n+1):
    sum = sum + 1/(i**2)

# Xử lý dấu thập phân
sum = str(round(sum, 3)) # làm tròn 3 chữ số thập phân
sum = sum.replace('.', ',', 1) # thay dấu chấm . bởi dấu phẩy ,

# Ghi file output
fo = open('cau1.out','w')
fo.write(sum)
fo.close()
