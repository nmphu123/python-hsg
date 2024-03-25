# Hàm đếm số lượng ước
def count_divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1

# Đọc file input
fi = open('cau3.inp')
n = int(fi.readline())
fi.close()

# Ghi file output
fo = open('cau3.out','w')

# Thuật toán xử lý
if count_divisor(n) % 2 == 0:
    fo.write('EVEN')
else:
    fo.write('ODD')
