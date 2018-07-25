#Chuyễn mỗi ký tự tab thành ký tự space.
#Xác nhận kết quả lần lượt bằng các lệnh sed, tr, và expand.
import re

def tap_to_space(filename):
	with open(filename,'rU') as f:
		for line in f:
			result = re.sub(r'\t', ' ', line)
			print(result)
	f.close
	
f="hightemp.txt"
tap_to_space(f)