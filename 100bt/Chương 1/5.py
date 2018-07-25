#Viết hàm sinh ra tất cả các n-gram từ một dãy cho trước (xâu ký tự hoặc danh sách).
str='I am an NLPer'

def C_gram(str):
	#n=str.split()
	n=str[:]
	print(type(n))
	i=0

	while i<len(n):
		if n[i]!=' ':
			print(n[i],str.count(n[i]),)
	#print(n.count(n[i]))
		i+=1
def N_gram(str):
	n=str.split()
	i=0
	while i<len(n):
		if n[i]!=' ':
			print(n[i],n.count(n[i]),)
	#print(n.count(n[i]))
		i+=1
def Bi_gram(str):
	n=str[:]
	i=0
	while i<len(n)-1:
		if (n[i]!=' ' and n[i+1]!=' '):
			n_i=str[i:i+2]
			print(n_i,str.count(n_i),)
	#print(n.count(n[i]))
		i+=1
N_gram(str)		
print('---')
C_gram(str)
print('---')
Bi_gram(str)
