#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print('Kteam' + str(69))
print('Kteam', 69)
print(123, [1, 2, 3], 'Kteam')
#sep
print('Kteam', 'Python', 'Course') # sep mặc định là 1 khoảng trắng
#Kteam Python Course
print('Kteam', 'Python', 'Course', sep='---')
#Kteam---Python---Course
print('Kteam', 'Python', 'Course', sep='|||')
#Kteam|||Python|||Course
print('Kteam', 'Python', 'Course', sep='\n')
#Kteam
#Python
#Course
print('Kteam', 'Python', 'Course', sep='')
#KteamPythonCourse
#end
print('a line without newline', end='')
#a line without newline
print('a line without newline', end='|||')
#a line without newline|||
print()

from time import sleep # nhập hàm sleep từ thư viện time

print('start....')
sleep(3) # dừng chương trình 3 giây
print('end...')

from time import sleep # nhập hàm sleep từ thư viện time

print('start....', end='') # in ra nội dung và kết thúc bới một chuỗi  rỗng.Ko in ra nga vì sau start ko có newline
sleep(3) # dừng chương trình 3 giây
print('end...')
#sửa lỗi trên
from time import sleep # nhập hàm sleep từ thư viện time

print('start...', end='', flush=True)
sleep(3) # dừng chương trình 3 giây
print('end...')

from time import sleep # nhập hàm sleep từ thư viện time

print('line 1\n', 'line2', end='')
sleep(3) # dừng chương trình 3 giây
print('end')

with open('printtext.txt', 'w') as f:
	print('printed by print function', file=f)

with open('printtext.txt') as f:
	f.read()

from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for a in your_great + your_name:
    print(a, end='', flush=True)
    sleep(0.1)
print()