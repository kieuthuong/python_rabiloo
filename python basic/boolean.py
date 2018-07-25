print(3>1 & 3<1)
print(ord('a'))
print(ord('b')>ord('k'))
print('aaa'<'aaaAd')

lst = [1, 2, 3]
lst_ = [1, 2, 3]
print(lst == lst_) #true
print(lst is lst_) #false
_lst = lst
print(_lst is lst)#true 
#dùng is sexdungf id để ss
#Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự dưới 20
# thì các biến có cùng một giá trị sẽ có cùng một giá trị trả về từ hàm id.
a=2
b = -4
print( b < -3 < -1 < 0 < a < 6)