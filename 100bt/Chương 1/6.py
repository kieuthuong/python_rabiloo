def X(str):
	n=str[:]
	i=0
	x=set()
	while i<len(n)-1:
		if (n[i]!=' ' and n[i+1]!=' '):
			n_i=str[i:i+2]
			x.add(n_i)
		i+=1
	return x
strX= "paraparaparadise"
strY= "paragraph"
union=X(strX) |X(strY) #phép hợp
intersection=X(strX) & X(strY) #phép giao
difference=X(strX) - X(strY) #phép trừ
print('Tập bi-gram của A:',X(strX))
print('Tập bi-gram của B:',X(strY))
print('union(A,B) =',union)
print('intersection(A,B) = ' ,intersection)
print('difference(A,B) = ',difference)
print("'se'có trong X :",'se' in X(strX))