# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

# Hàm tìm ước nguyên tố lớn nhất của một số
def gpd(n):
    if is_prime(n):
        return n
    for i in range(n//2+1, 1, -1):
        if n % i == 0 and is_prime(i):
            return i

# Đọc file input
fi = open('cau2.inp')
a = int(fi.readline())
fi.close()

# Thuật toán xử lý
gpd = gpd(a)
count = 1
i = 1

# Ghi file output
fo = open('cau2.out','w')
fo.write(str(gpd)+' ')
while count < 5:
    i = i + 1
    if gpd(gpd*i) == gpd:
        fo.write(str(gpd*i)+' ')
        count = count + 1
fo.close()
