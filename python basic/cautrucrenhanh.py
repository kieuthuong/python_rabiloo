a = 2
b = 0
if a - 1 < 0: # (a – 1 < 0) có giá trị là True
	print('a nhỏ hơn 1')
if b - 1 < 0: # (b – 1  < 0) có giá trị là False
    print('b nhỏ hơn 1')

if a - 1 < 0: # (a – 1 < 0) có giá trị là True
	print('a nhỏ hơn 1')
	if b - 1 < 0:
    	 print('b nhỏ hơn 1')


if a - 1 < 0: # False, tiếp tục
    print('a nhỏ hơn 1')
elif a - 2 < 0: # False, tiếp tục
     print('a nhỏ hơn 2')
elif a - 3 < 0: # False, tiếp tục
     print('a nhỏ hơn 3')
elif a - 4 < 0: # True, kết thúc
     print('a nhỏ hơn 4')
elif a - 5 < 0: # Khối BIG đã kết thúc, dù đây là True nhưng không ý nghĩa
     print('a nhỏ hơn 5')
#Những dòng code cùng lề thì là cùng một block.
#Một block có thể có nhiều block khác.
#Khi căn lề block không sử dụng cả tab lẫn space.
#Nên sử dụng 4 space để căn lề một block
k1 = int(input('Nhap so thu nhat\n=> '))
k2 = int(input('Nhap so thu hai\n=> '))
k3 = int(input('Nhap so thu ba\n=> '))

if k1 > k2 and k1 > k3:
    print('so lon nhat la', k1)
elif k2 > k1 and k2 > k3:
    print('so lon nhat la', k2)
else:
    print('so lon nhat la', k3)
    #chạy
   #Tools->SublimeREPL->Python->Python-Run