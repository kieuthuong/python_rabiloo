#Đếm số dòng trong file. Xác nhận kết quả bằng lệnh wc trong unix.
def count_line(filename):
	pass
	sum_line=0
	with open(filename) as f:
		for line in f:
			if line.strip(): #chuỗi đã cắt đi khoảng trắng ở đầu và cuối
				sum_line+=1
	print(sum_line)
	f.close()

f="hightemp.txt"
count_line(f)
