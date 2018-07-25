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
	
	p1=yes/total
	p2=no/total
	#trường hợp của lớp yes
	out_yes=0
	temp_yes=0
	warm_yes=0
	wind_yes=0

	out_no=0
	temp_no=0
	warm_no=0
	wind_no=0
	
	out_0_yes=0
	out_1_yes=0
	out_2_yes=0
	temp_0_yes=0
	temp_1_yes=0
	temp_2_yes=0
	warm_0_yes=0
	warm_1_yes=0
	wind_0_yes=0
	wind_1_yes=0

	out_0_no=0
	out_1_no=0
	out_2_no=0
	temp_0_no=0
	temp_1_no=0
	temp_2_no=0
	warm_0_no=0
	warm_1_no=0
	wind_0_no=0
	wind_1_no=0
	
	#ngoài trời
	for x in range(total):
		if list[x][0]=='0':
			if list[x][4]=='1':
				out_0_yes+=1
				out_yes+=1
			else:
				out_0_no+=1
				out_no+=1
		elif list[x][0]=='1':
			if list[x][4]=='1':
				out_1_yes+=1
				out_yes+=1
			else:
				out_1_no+=1
				out_no+=1
		elif list[x][0]=='2':
			if list[x][4]=='1':
				out_2_yes+=1
				out_yes+=1
			else:
				out_2_no+=1
				out_no+=1

	#print(out_yes,out_0_yes,out_1_yes,out_2_yes)
	#print(out_no,out_0_no,out_1_no,out_2_no)

	p_out_yes=0
	p_out_no=0
	if ngoai_troi==0:
		p_out_yes=out_0_yes/out_yes
		p_out_no=out_0_no/out_no
	elif ngoai_troi==1:
		p_out_yes=out_1_yes/out_yes
		p_out_no=out_1_no/out_no
	elif ngoai_troi==2:
		p_out_yes=out_2_yes/out_yes
		p_out_no=out_2_no/out_no
	
	
	#nhiệt độ
	for x in range(total):
		if list[x][1]=='0':
			if list[x][4]=='1':
				temp_0_yes+=1
				temp_yes+=1
			else:
				temp_0_no+=1
				temp_no+=1
		elif list[x][1]=='1':
			if list[x][4]=='1':
				temp_1_yes+=1
				temp_yes+=1
			else:
				temp_1_no+=1
				temp_no+=1
		elif list[x][1]=='2':
			if list[x][4]=='1':
				temp_2_yes+=1
				temp_yes+=1
			else:
				temp_2_no+=1
				temp_no+=1
	p_temp_yes=0
	p_temp_no=0
	if nhiet_do==0:
		p_temp_yes=temp_0_yes/temp_yes
		p_temp_no=temp_0_no/temp_no
	elif nhiet_do==1:
		p_temp_yes=temp_1_yes/temp_yes
		p_temp_no=temp_1_no/temp_no
	elif nhiet_do==2:
		p_temp_yes=temp_2_yes/temp_yes
		p_temp_no=temp_2_no/temp_no
	
	#độ ấm
	for x in range(total):
		if list[x][2]=='0':
			if list[x][4]=='1':
				warm_0_yes+=1
				warm_yes+=1
			else:
				warm_0_no+=1
				warm_no+=1
		elif list[x][2]=='1':
			if list[x][4]=='1':
				warm_1_yes+=1
				warm_yes+=1
			else:
				warm_1_no+=1
				warm_no+=1
	p_warm_yes=0
	p_warm_no=0
	if do_am==0:
		p_warm_yes=warm_0_yes/warm_yes
		p_warm_no=warm_0_no/warm_no
	elif do_am==1:
		p_warm_yes=warm_1_yes/warm_yes
		p_warm_no=warm_1_no/warm_no
	
	#gió
	for x in range(total):
		if list[x][3]=='0': 
			if list[x][4]=='1':
				wind_0_yes+=1
				wind_yes+=1
			else:
				wind_0_no+=1
				wind_no+=1
		elif list[x][3]=='1':
			if list[x][4]=='1':
				wind_1_yes+=1
				wind_yes+=1
			else:
				wind_1_no+=1
				wind_no+=1
			
	p_wind_yes=0
	p_wind_no=0
	if gio==0:
		p_wind_yes=wind_0_yes/wind_yes
		p_wind_no=wind_0_no/wind_no
	elif gio==1:
		p_wind_yes=wind_1_yes/wind_yes
		p_wind_no=wind_1_no/wind_no
	

	#so sanh va du doan
	x1=p1*p_out_yes*p_temp_yes*p_warm_yes*p_wind_yes
	print(x1,p_out_yes,p_temp_yes,p_warm_yes,p_wind_yes)
	x2=p2*p_out_no*p_temp_no*p_warm_no*p_wind_no
	print(x2,p_out_no,p_temp_no,p_warm_no,p_wind_no)
	if x1>x2:
		print("Dự đoán sẽ đi")
	else:
		print("Dự đoán ko đi")


guess(0,0,0,0)
guess(1,1,1,1)
guess(2,2,0,0)