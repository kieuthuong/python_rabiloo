
def play(ngoai_troi,nhiet_do,do_am,gio):
	p1=8/12 #co di 1
	p2=4/12 #khong di 0
	p_ngoaitroi_1=0
	p_nhietdo_1=0
	p_doam_1=0
	p_gio_1=0
	p_ngoaitroi_2=0
	p_nhietdo_2=0
	p_doam_2=0
	p_gio_2=0
	if ngoai_troi==0:#nang
		p_ngoaitroi_1=2/5
	elif ngoai_troi==1:#amu
		p_ngoai_1=3/3
	elif ngoai_troi==2:#mua
		p_mua_1=3/4
	if nhiet_do==0:#nong
		p_nhietdo_1=1/3
	elif nhiet_do==1:#binh thuong
		p_nhietdo_1=5/5
	elif nhiet_do==2:#matme
		p_nhietdo_1=3/4
	if do_am==0:#cao
		p_doam_1=3/6
	elif do_am==1:#binh thuong
		p_doam_1=5/6
	if gio==0:#manh
		p_gio_1=3/5
	elif gio==1:#yeu
		p_gio_1=5/7
	
	if ngoai_troi==0:#nang
		p_ngoaitroi_2=3/5
	elif ngoai_troi==1:#amu
		p_ngoai_2=0/3
	elif ngoai_troi==2:#mua
		p_mua_2=1/4
	if nhiet_do==0:#nong
		p_nhietdo_2=2/3
	elif nhiet_do==1:#binh thuong
		p_nhietdo_2=0/5
	elif nhiet_do==2:#matme
		p_nhietdo_2=1/4
	if do_am==0:#cao
		p_doam_2=3/6
	elif do_am==1:#binh thuong
		p_doam_2=1/6
	if gio==0:#manh
		p_gio_2=2/5
	elif gio==1:#yeu
		p_gio_2=2/7

	#print( p1*p_doam_1)
	x1=p1*p_ngoaitroi_1*p_nhietdo_1*p_doam_1*p_gio_1
	x2=p2*p_ngoaitroi_2*p_nhietdo_2*p_doam_2*p_gio_2
,
	if x1>x2:
		print("Dự đoán sẽ đi")
	else:
		print("Dự đoán ko đi")

play(1,0,0,0)