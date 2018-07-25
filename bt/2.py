def play(ngoai_troi,nhiet_do,do_am,gio):
	list = [[0,0,0,0,0],[0,0,0,1,0],[1,0,0,0,1],[2,1,0,0,1],[2,2,1,0,1],
	[2,2,1,1,0],[1,2,1,1,1],[0,1,0,0,0],[0,2,1,0,1],[2,1,1,0,1],[0,1,1,1,1],[1,1,0,1,1]]
	#print (list)
	#0:nang nong cao yeu
	#1 amu binhthuong binhthuong yeu
	#2 mua mat me
	#print(list[1][1])
	yes=0
	no=0
	play=0
	print(len(list))
	for x in range(len(list)):
		if list[x][4]==1:
			yes+=1
			play+=1
		else:
			no+=1
			play+=1

	p1=yes/play
	p2=no/play
	ngoai_troi_nang_1=0
	ngoai_troi_amu_1=0
	ngoai_troi_mua_1=0
	ngoai_troi_1=0
	nhiet_do_1=0
	nhiet_do_nong_1=0
	nhiet_do_binhthuong_1=0
	nhiet_do_matme_1=0
	do_am_1=0
	do_am_cao_1=0
	do_am_binhthuong_1=0
	gio_1=0
	gio_yeu_1=0
	gio_manh_1=0
	y=0
	
	#if y==0:
	for x in range(play):
		if list[x][0]==0 and list[x][4]==1:
			ngoai_troi_nang_1+=1
			ngoai_troi_1+=1
		elif list[x][0]==1 and list[x][4]==1:
			ngoai_troi_amu_1+=1
			ngoai_troi_1+=1
		elif list[x][0]==2 and list[x][4]==1:
			ngoai_troi_mua_1+=1
			ngoai_troi_1+=1
	#if y==1:
	for x in range(12):
		if list[x][1]==0 and list[x][4]==1:
			nhiet_do_nong_1+=1
			nhiet_do_1+=1
		elif list[x][1]==1 and list[x][4]==1:
			nhiet_do_binhthuong_1+=1
			nhiet_do_1+=1
		elif list[x][1]==2 and list[x][4]==1:
			nhiet_do_matme_1+=1
			nhiet_do_1+=1
	#elif y==2:
	for x in range(12):
		if list[x][2]==0 and list[x][4]==1:
			do_am_cao_1+=1
			do_am_1+=1
		elif list[x][2]==1 and list[x][4]==1:
				do_am_binhthuong_1+=1
				do_am_1+=1
	#elif y==3:
	for x in range(12):
		if list[x][3]==0 and list[x][4]==1:
			gio_yeu_1+=1
			gio_1+=1
		elif list[x][3]==1 and list[x][4]==1:
			gio_manh_1+=1
			gio_1+=1
	
	
	p_ngoai_troi_nang_1=ngoai_troi_nang_1/ngoai_troi_1
	p_ngoai_troi_amu_1=ngoai_troi_amu_1/ngoai_troi_1
	p_ngoai_troi_mua_1=ngoai_troi_mua_1/ngoai_troi_1
	p_nhiet_do_nong_1=nhiet_do_nong_1/nhiet_do_1
	p_nhiet_do_binhthuong_1=nhiet_do_binhthuong_1/nhiet_do_1
	p_nhiet_do_matme_1=nhiet_do_matme_1/nhiet_do_1
	p_do_am_cao_1=do_am_cao_1/do_am_1
	p_do_am_binhthuong_1=do_am_binhthuong_1/do_am_1
	p_gio_yeu_1=gio_yeu_1/gio_1
	p_gio_manh_1=gio_manh_1/gio_1

	p_ngoai_troi_1=0
	p_nhiet_do_1=0
	p_do_am_1=0
	p_gio_1=0
	if ngoai_troi==0:
		p_ngoai_troi_1=p_ngoai_troi_nang_1
	elif ngoai_troi==1:		
		p_ngoai_troi_1=p_ngoai_troi_amu_1
	elif ngoai_troi==2:			
		p_ngoai_troi_1=p_ngoai_troi_mua_1
	if nhiet_do==0:
		p_nhiet_do_1=p_nhiet_do_nong_1
	elif nhiet_do==1:		
		p_nhiet_do_1=p_nhiet_do_binhthuong_1
	elif  nhiet_do==2:			
		p_nhiet_do_1=p_nhiet_do_matme_1		
	if do_am==0:
		p_do_am_1=p_do_am_cao_1
	elif do_am==1:
		p_do_am_1=p_do_am_binhthuong_1
	if gio==0:
		p_gio_1=p_gio_yeu_1
	elif gio==1:
		p_gio_1=p_gio_manh_1
	p_ngoai_troi_2=1-p_ngoai_troi_1
	p_nhiet_do_2=1-p_nhiet_do_1
	p_do_am_2=1-p_do_am_1
	p_gio_2=1-p_gio_1
	
	x1=p1*p_ngoai_troi_1*p_nhiet_do_1*p_do_am_1*p_gio_1
	x2=p2*p_ngoai_troi_2*p_nhiet_do_2*p_do_am_2*p_gio_2
	if x1>x2:
		print("Dự đoán sẽ đi")
	else:
		print("Dự đoán ko đi")
play(0,0,0,0)