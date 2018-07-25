#Được giới hạn bởi cặp {}
#Set ko chứa nhiều hơn một phần tử trùng lặp
#không thể chứa 1 set trong 1 set
set_1={69,96}
print(set_1)
print(type(set_1))
#K tao dc mot empty set
set_2=set('How Kteam')
print(set_2)
print(type(set_2))

print(1 in {1,2,4})
print({1,2,3}-{1})
print({1,2}-{1,2})
print({1,4,5}&{1,6,7})
print({1,3,4}^{5})
set1={1,2,3}
set2={3,4}

set3=set1 & set2
set4=set1 | set2
set5=set3 - set4
print('a',set3)
print('b',set4)
print('c',set5)
#set ko quan tâm đến vị trí của ptu trong set nên ko thể cắt và sáp xếp
#Các phương thức cơ bản
set5.clear()
print(set5)
set1.pop()#lấy ra thằng đầu tiên đồng thời xóa nó khỏi set
print(set1)
set1.remove(2)
print(set1)
set11=set1.copy()
print(set11)
#phương thức add thêm value vào set,nếu đã có bỏ qua
set1.add(2)
set1.add(1)
set1.add(4)
print(set1)

seta={1,2,3}
setb=seta
setb.clear()#clear b thì a cũng rỗng
print('result',seta)
#Ta đã cho a,b trỏ vào cùng 1 chỗ do đó thay đổi b thì a cũng sẽ bị tác động
#Muốn giải quyết sử dụng phương thức copy

