help(open)
file_object = open('file1.txt')
data = file_object.read()
print(data)
#muốn đọc file lần nữa phải đóng rồi mở fille lần nữa vifcon trỏ đang ở cuối file
file_object.close()
file_object = open('file1.txt')


data2 = file_object.readline()
print(data2)
file_object.close()
#đọc hết các dòng và cho nó vào một list
file_object=open('file1.txt')
data3 = file_object.readlines()
print(data3)
file_object.close()
file_object=open('file1.txt',mode='a+') 
#nếu thay a bằng w nó sẽ xóa hết nội dung cũ trước khi cập nhật nội dung mới
#data4 = file_object.write('\n12/03/1997')
#file_object.close()
#print(data4)

file_object = open('file1.txt')
data5 = file_object.read()
print(data5)
file_object.seek(0)#quay đầu con trỏ về chỉ số bên trong
data6 = file_object.read(5)
print(data6)