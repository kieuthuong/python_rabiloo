#giới hạn bởi cawpk ngoặc []
#các phaaanfb tử của list cách nhau bởi dấu phẩy
#list có khả năng chứa mọi giá trị của đối tượng của python
a=[i for i in range(30)]
b=[[n,n*1,n*2] for n in range(1,6)]
print(a)
print(b)
c=[1,2]
c+=['one','two']
print(c)
#không được phép gán list này sang list kia nếu o có chủ đích.Vì khí đó thay đổi 1 list làm thay đổi list còn lại
#ma trận
m=[[1,2,3],[4,5,6],[7,8,9]]
print(m[0])
print(m[1])
print(m[2])
print(m[0][2])
#các phương thức cho list
k=[1,2,3,4,5,6,7]
print(k.count(1))
print(k.index(1))
k1=k.copy()
k1[0]='xxx'
print(k)
print(k1)
k1=k.clear()
print(k)
k.append([1,2])
print(k)
k.extend([2,3,[4,5]])
print(k)
k.insert(1,'thuong')
print(k)
print(k.pop(1))
k.remove(2)
print(k)

k2=[1,5,7,3,4]
k2.reverse()#dao vi tri
print(k2)
k2.sort(reverse=True)
print(k2)#sap xep tang neu reverse=False
