#Bài 1
#Cho một file text tên draft.txt
#Trong file này có một số chữ Kteam (Kteam sẽ không xuất hiện ở đầu dòng), 
#và trước nó là một chữ ngẫu nhiên nào đó và nhiệm vụ của bạn là đổi chữ 
#đó thành How. Nhớ là sử dụng vòng lặp.

#Sau khi đổi thành công, bạn lưu nội dung đó vào file tên kteam.txt.

with open('draft.txt') as f:
	#lay nd file duoidang mot list
	data=f.readlines()

i=0#mốc bắt đầu
length=len(data)#mốc kết thúc
new_content = ''#nội dung mới

while i < length:
	#tách một dòng thành một list
	line_list = data[i].split()
	i_line=0
	length_line=len(line_list)
	while i_line<length_line:
		if line_list[i_line]=='Kteam' or line_list[i_line]=='kteam':
			line_list[i_line - 1]='How'
		i_line+=1
	#nối lại thành một dòng
	new_content += ' '.join(line_list) + '\n'
	i+=1

with open('new_dralt.txt','w') as new_f:
	new_f.write(new_content)

#Bai 2
#Sắp xếp một mảng số nguyên có dạng như sau:
#[56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
#là các số 11 là những số cố định không được thay đổi vị trí của nó.

lst = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]
idx = 0
max_idx = len(lst) - 1

max_jdx = len(lst)

while idx < max_idx:
    if lst[idx] == 11:
        idx += 1
        continue
    jdx = idx + 1
    while jdx < max_jdx:
        if lst[jdx] == 11:
            jdx += 1
            continue
        if lst[idx] > lst[jdx]:
            lst[idx], lst[jdx] = lst[jdx], lst[idx]
        jdx += 1
    idx += 1
print('Chuỗi sau khi sắp xếp : ')
print(lst)