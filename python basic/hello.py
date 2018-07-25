print("Hello ") #dkvbx
#dữ liệu kiểu số
a = 4 #intergers
print(a)
print(type(a))
b=15.049563854950354837458941
print(b)
#lay toan bo noi dung cua tv decimal
from decimal import*
#llấy tối đa 30 chữ số phần guyên và phần thập phân
getcontext().prec = 30
print(Decimal(10)/Decimal(3))
#ham phan so
from fractions import*
c=Fraction(6,9)
print(c)
#kieu so thuc
d=complex(2,5)
print(d)
print(d.real)
print(d.imag)
#chia lay nguyen lay du
print(10//3)
print(10%3)
print(10**3)
#thu vien math
import math
print(math.trunc(3.6))
print(math.floor(3.6))
print(math.ceil(3.6))
print(math.fabs(-3.6))
print(math.sqrt(4))
print(math.gcd(7,11)) #UCLN(7,11)
#String
print('Student')
print("I'm Student")
print('"Student"')
str='''
1
2
sdlcxm
'''
print(str)
#tieng chuong
print('\a')
print('assgd \naksgz')
print(r'assgd \naksgz')
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