# Đọc file input
fi = open('cau3.inp')
n = int(fi.readline())
a = fi.readline().split()
for i in range(n):
    a[i] = int(a[i]) # Chuyển list a về số nguyên
fi.close()

# Hàm kiểm tra số tự mãn trả về boolean
def is_narcissistic(m):
    cube_sum = 0
    for i in str(m):
        cube_sum = cube_sum + int(i)**3
    if cube_sum == m:
        return True
    return False

# Thuật toán xử lý
b = []
for i in a:
    if is_narcissistic(i):
        b.append(i)
b.sort() # Sắp xếp mảng b tăng dần

# Ghi file output
fo = open('cau3.out','w')
for i in b:
    fo.write(str(i)+' ')
fo.close()
