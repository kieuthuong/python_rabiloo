k=5
while k>0:
	print('k=',k)
	k-=1

s='How are you'
idx = 0 # vị trí bắt đầu bạn muốn xử lí của chuỗi
length = len(s) # lấy độ dài chuỗi làm mốc kết thúc
while idx<length:
	print(idx,s[idx])
	idx+=1
#list va tuple hoan toan tuong tu

#Cau lenh break
five_even_numbers = []
k_number = 1

while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn         
    	five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
    if len(five_even_numbers) >= 5: # nếu list này đủ 5 phần tử
        break # thì kết thúc vòng lặp
    k_number += 1
print(five_even_numbers)
print(k_number)

#Cau lenh continue
k1_number = 0
while k1_number < 10:
	k1_number+=1
	if k1_number % 2 == 0:
		continue
	print(k1_number,'is odd number')

#Cau lenh while-else
k = 0
while k<3:
	print('value of k is' , k)
	k+=1
else:
	print('k is not less than 3 anymore')

k1 = 0
while  k1<5:
	print('value',k1)
	k1+=1
	if k1>3:
		print('k is greater than 3')
		break
else:
	print('k is not less than 5 anymore')