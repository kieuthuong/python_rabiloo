#in chi tra lai mot trong hai gia tri true or false
strA=('rabiloo')
strB=('u')
strC=strB in strA
#lay chuoi cat chuoi
print(strC)
print(strA[0])
print(strA[-2])
print(strA[len(strA)-1])
strD=strA[3:len(strA)]
print(strD)
#cat theo [tu:den:buoc nhay]
strE = strA[None:None:3]
print(strE)
#in ra chuoi 
e='My name is %s %d'%("Thuong",5)
print(e)
s='%s %s'
result=s %('hai','ba')
print(result)
print(f'a\tb')
Kteam='Kteam'
result=f'{Kteam}- Free education'
print(result)
#gan,can le
r= '1: {one},2: {two}' .format(one=111,two=777)
print(r)
l='How{:*^50}Free education'.format('Kteam')
l1='Nguyen{:<30}Thuong'.format('')
print(l)
print(l1)
#Kieu chuoi
#viet hoa dau dong
a1='how kteam'
b1=a1.capitalize()
print(b1)
c1=a1.swapcase()
print(c1)
d1=a1.title()
print(d1)
e1=a1.center(50,'*')
print(e1)
g1=a1.join(['1','2','3'])
print(g1)
h1=a1.replace('o','a',1)#thay o thanh a
print(h1)
t1=a1.strip('h')#cat hai dau
print(t1)

a2='how kteam free education'
b2=a2.split('e',2)#cat theo ki tu va so lan cat trong split .rsplit cat tu ben phai
print(a2)
print(b2)
c2=a2.partition('k')#cat truoc sau va chu k
d2=a2.count('t',0,6)
e2=a2.startswith('how',6)
print(e2)
g2=a2find('kteam')