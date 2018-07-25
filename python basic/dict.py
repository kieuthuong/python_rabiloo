#Được giới hạn bởi ngoặc nhọn,các phần tử phân cách bằng dấu phẩy,cặp key : value là 1 phần tử
#key value kiểu gì cũng dc mà luôn đi theo cặp
dic={'name':'Thuong','tuoi':20}
print(dic)
print(type(dic))
#mapping object gần giống với dict object
#một object là một mapping object khi có đủ hai phương thức keys và _getitem_
#một dict object cũng là một mapping object.Tuy nhiên ,ko phải mapping object nào cũng là dict object 
#vì dict object ko chỉ có keys:getitem mà còn nhiều phương thức khác

#khởi tạo bằng iterable
#bạn có thể dùng list ,tuple hay bất cứ container nào (trừ mapping object)để chứa cặp key-value
iter_=[('name','Thuong'),('tuoi',20)]
dic1=dict(iter_)
print(dic1)
print(type(dic1))

#khởi tạo bằng keywords argument
#bạn khởi tạo biến và giá trị rồi đưa dict đó giữ giùm
#các biến này không bị ảnh hưởng hoặc ảnh hưởng gì tới các biến bên ngoài
name='ten'
age='tuoi'
dic2=dict(name='Thuong',age=20)
print(dic2)
print(type(dic2))

#sử dụng cu pháp khởi tạo fromkey
iter__=('name','age')
dic3=dict.fromkeys(iter__)
print(dic3)
print(type(dic))
dic3=dict.fromkeys(iter__,3)
print(dic3)

#lấy value bằng key
print(dic3['name'])
dic3['name']='Thuong'
print(dic3['name'] , dic3['age'])
#gan thêm key chưa có trong dict nó sẽ tự động lưu vào dict
dic3['birthday']='12/03/1997'
print(dic3['birthday'])
print(dic3)
dic3["age"]=3+5
dic3['name']+=' Nguyen'
print(dic3)

#phương thức copy()
d={'Team':'Kteam',(1,2):69}
print(d)
d2=d.copy()#copy tạo ra một bản sao ở một vùng nhớ mới
print(d2)
value=d.get("Team")#get lấy ra giá trị của key team
print(value)

value1=d.items()
print(value1)
value2=d.keys()
print(value2)
value3=d.pop('Team')#cho ra và xóa luôn
print(value3)
print(d)
print(d.pop('sss','thêm value là ko lỗi dù key ko có trong dict'))

value5 = d.setdefault('Team')
print(value5)
print(d)
d1={'Team1':'Kteam',(1,3):69}
d.update(d1)
print(d)
value=d.update(Team1='update value')
print(d)