#iterator dùng để lấy lần lượt từng giá trị
itera = (x for x in range(3)) #cac tao
print(next(itera))#next truy xuất lần lượt các giá trị trong iterator
iterb=itera#cùng trỏ về 1,vợ chồng cùng 1 tk.

#trả về tổng các giá trị cộng thêm vào chỉ số sau ,
print(sum(itera,2))
#sum sẽ đưa trỏ về cuối danh sách

print(max(5,6))
print(sorted([1, 6, 7, 2], reverse=True))