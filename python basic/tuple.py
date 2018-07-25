#được giới hạn bởi cặp ()
#các phần tử phân cách nhau bởi ,
#tuple có khả năng chứa mọi giá trị
#tốc đọ truy xuất của tuple nhanh hơn list
#dung lượng chiếm trong bộ nhớ nhỏ hơn list		
#bảo vệ dữ liệu của bạn sẽ không bị thay đổi
#có thể dùng tạm key của dictionary

tup=(i for i  in range(10) if i % 2==0)
a=tuple(tup)
b=tuple('kteam')
print(a)
print(b)

tup1=(1,2,3)
tup1+=(4,5,6)
print(tup1)
tup1*=5
print(tup1)
print(1 in tup1)
print(tup1[4])
print(len(tup1))
a1=tup1[len(tup1)-1]
print(a1)
print(tup1[-1])
print(tup1[::-1])
print(tup1[1:5])

tup2=((1,2,3),(4,5,6),(7,8,9))
print(tup2)
print(tup2.count(1))
#Khi nào nên dùng tuple thay cho list
