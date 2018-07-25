def matrix(file):
	contents = open(file).read()
	return [item.split() for item in contents.split('\n')[:-1]]


def guess(ngoai_troi,nhiet_do,do_am,gio):
	list=matrix('myfile.txt')
	print(list)
	#0:nắng,nóng,cao,yếu
	#1:âm u, bình thường,mạnh
	#2:mưa, mát mẻ
	yes=0 #1
	no=0  #0
	total=len(list)
	#tính tổng số ngày đi và không đi
	for x in range(total):
		if list[x][4]=='1':
			yes+=1
		else:
			no+=1
	
	p1=yes+1/total+2
	p0=no+1/total+2
	#trường hợp của lớp yes
	#tổng những ngày đi 
	out=0
	temp=0
	warm=0
	wind=0
	
	out_0=0
	out_1=0
	out_2=0
	temp_0=0
	temp_1=0
	temp_2=0
	warm_0=0
	warm_1=0
	wind_0=0
	wind_1=0
	
	#ngoài trời
	for x in range(total):
		if list[x][0]=='0' and list[x][4]=='1':
			out_0+=1
			out+=1
		elif list[x][0]=='1' and list[x][4]=='1':
			out_1+=1
			out+=1
		elif list[x][0]=='2' and list[x][4]=='1':
			out_2+=1
			out+=1
	out_0_total=0#tong tat ca ngay nang
	out_1_total=0#tong tat ca ngay am u
	out_2_total=0#tong tat ca ngay mua
	for x in range(total):
		if list[x][0]=='0':
			out_0_total+=1
	for x in range(total):
		if list[x][0]=='1':
			out_1_total+=1
	for x in range(total):
		if list[x][0]=='2':
			out_2_total+=1
	
	p_out=0
	if ngoai_troi==0:
		p_out=out_0+1/out_0_total+3
	elif ngoai_troi==1:
		p_out=out_1+1/out_1_total+3
	elif ngoai_troi==2:
		p_out=out_2+1/out_1_total+3
	
	#nhiệt độ
	for x in range(total):
		if list[x][1]=='0' and list[x][4]=='1':
			temp_0+=1
			temp+=1
		elif list[x][1]=='1' and list[x][4]=='1':
			temp_1+=1
			temp+=1
		elif list[x][1]=='2' and list[x][4]=='1':
			temp_2+=1
			temp+=1
	temp_0_total=0#tong tat ca ngay nong
	temp_1_total=0#tong tat ca ngay bình thường
	temp_2_total=0#tong tat ca ngay mát mẻ
	for x in range(total):
		if list[x][1]=='0':
			temp_0_total+=1
	for x in range(total):
		if list[x][1]=='1':
			temp_1_total+=1
	for x in range(total):
		if list[x][1]=='2':
			temp_2_total+=1
	p_temp=0
	if nhiet_do==0:
		p_temp=temp_0+1/temp_0_total+3
	elif nhiet_do==1:
		p_temp=temp_1+1/temp_1_total+3
	elif nhiet_do==2:
		p_temp=temp_2+1/temp_1_total+3
	
	#độ ấm
	for x in range(total):
		if list[x][2]=='0' and list[x][4]=='1':
			warm_0+=1
			warm+=1
		elif list[x][2]=='1' and list[x][4]=='1':
			warm_1+=1
			warm+=1
	warm_0_total=0#tong tat cả ngày độ ấm cao
	warm_1_total=0#tong tất cả này độ ấm bình thường
	for x in range(total):
		if list[x][2]=='0':
			warm_0_total+=1
	for x in range(total):
		if list[x][2]=='1':
			warm_1_total+=1
	p_warm=0
	if do_am==0:
		p_warm=warm_0+1/warm_0_total+2
	elif do_am==1:
		p_warm=warm_1+1/warm_1_total+2
	
	
	#gió
	for x in range(total):
		if list[x][3]=='0' and list[x][4]=='1':
			wind_0+=1
			wind+=1
		elif list[x][3]=='1' and list[x][4]=='1':
			wind_1+=1
			wind+=1
	for x in range(total):
		if list[x][2]=='0' and list[x][4]=='1':
			warm_0+=1
			warm+=1
		elif list[x][2]=='1' and list[x][4]=='1':
			warm_1+=1
			warm+=1
	wind_0_total=0#tong tat cả gió yếu
	wind_1_total=0#tong tất cả gió mạnh
	for x in range(total):
		if list[x][3]=='0':
			wind_0_total+=1
	for x in range(total):
		if list[x][3]=='1':
			wind_1_total+=1
	p_wind=0
	if do_am==0:
		p_wind=wind_0+1/wind_0_total+2
	elif do_am==1:
		p_wind=wind_1+1/wind_1_total+2

	#xac suat trong lop NO
	p_out_no=1-p_out
	p_temp_no=1-p_temp
	p_warm_no=1-p_warm
	p_wind_no=1-p_wind

	#so sanh va du doan
	x1=p1*p_out*p_temp*p_warm*p_wind
	print(x1)
	print(p1,p_out,p_temp,p_warm,p_wind)
	print(p_temp)
	print(1-p_temp)
	print(p2,p_out_no,p_temp_no,p_warm_no,p_wind_no)
	x2=p2*p_out_no*p_temp_no*p_warm_no*p_wind_no
	print(x1,x2)
	if x1>x2:
		print("Dự đoán sẽ đi")
	else:
		print("Dự đoán ko đi")


guess(2,2,1,1)